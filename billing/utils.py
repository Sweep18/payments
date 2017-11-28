import decimal

from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from django.db.models import F
from django.db import transaction

from .models import CustomUser


@user_passes_test(lambda u: u.is_superuser)
def payment(request):
    user_list, numb_error = [], []
    users = CustomUser.objects.all()
    user = users.get(id=request.POST.get('user'))
    number = request.POST.get('number')
    number_list = number.replace(' ', '').replace('\r\n', '').split(',')
    amount_str = request.POST.get('amount')

    try:
        amount = decimal.Decimal(amount_str)
        if float(amount_str) < 0.01:
            return JsonResponse({'message': 'Введите сумму от 0.01'})

    except decimal.InvalidOperation:
        return JsonResponse({'message': 'Введите сумму от 0.01'})

    if user.wallet < amount:
        message = 'Недостаточно средств!'
    else:
        for numb in number_list:
            if numb:
                try:
                    us = users.get(number=numb)
                    if us == user:
                        return JsonResponse({'message': 'Вы не можете пополнить счет себе самому!'})

                    user_list.append(us)
                except CustomUser.DoesNotExist:
                    numb_error.append(numb)

        if numb_error:
            message = "ИНН %s не существует!" % numb_error
        else:
            count_user = len(user_list)

            if count_user == 0:
                return JsonResponse({'message': 'Введите ИНН'})

            part_amount = round(amount / count_user, 2)
            for user_pay in user_list:
                user_pay.wallet = F('wallet') + part_amount
                user.wallet = F('wallet') - part_amount
                with transaction.atomic():
                    user_pay.save(update_fields=('wallet',))
                    user.save(update_fields=('wallet',))
            message = 'Счета пополнены!'

    return JsonResponse({'message': message})
