from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class AdminCreateUserForm(UserCreationForm):

    number = forms.CharField(label='ИНН')
    wallet = forms.DecimalField(label='Счет', min_value=0, initial=0)

    def clean_number(self):
        number = self.cleaned_data.get('number')
        user = CustomUser.objects.filter(number=number)
        if user:
            text = "Такой ИНН уже зарегестрирован"
            raise forms.ValidationError(text)
        return number

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.number = self.cleaned_data["number"]
        user.wallet = self.cleaned_data["wallet"]
        return user


class PaymentForm(forms.Form):
    user = forms.ModelChoiceField(label='Пользователь', queryset=CustomUser.objects.all())
    number = forms.CharField(widget=forms.Textarea, label='ИНН(через запятую)', max_length=255)
    amount = forms.DecimalField(widget=forms.TextInput(), label='Сумма', decimal_places=2)
