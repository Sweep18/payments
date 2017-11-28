Напишите код приложения, используя Django 1.9 (или выше), в котором у пользователей есть помимо основных полей 2 дополнительных: ИНН и счет (в рублях, с точностью до копеек). Также необходимо реализовать форму, состоящую из полей:
 
Выпадающий список со всеми пользователями в системе, со счета которого нужно перевести деньги

Текстовое поле для ввода ИНН пользователей, на счета которых будут переведены деньги

Текстовое поле для указания какую сумму нужно перевести с одного счета на
другие
 
Необходимо проверять есть ли достаточная сумма у пользователя, со счета которого списываются средства, и есть ли пользователи с указанным ИНН в БД. При валидности введенных данных необходимо указанную сумму списать со счета указанного пользователя и перевести на счета пользователей с указанным ИНН в равных частях (если переводится 60 рублей 10ти пользователям, то каждому попадет 6 рублей на счет). Было бы неплохо, если бы форма работала без перезагрузки страницы.

Для запуска проекта:
1) Установить зависимости из requirements.txt
2) python manage.py runserver
3) Зайти на http://127.0.0.1:8000/
4) Логин: admin

    Пароль: qwerty123