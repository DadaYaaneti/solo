print('Привет, это программа для создания имя пользователя и пароля, помни,что заглавные буквы играют роль!')
z=input('Введите имя пользователя:')
a=input('Введите ваш новый пароль:')
b=input('Введите ваш новый пароль повторно:')
if a == b:
    print('Пароль успешно установлен!')
    g=input('Введите имя пользователя:')
    h=input('Введите пароль:')
    if z == g:
        if a == h:
            print('Успешно! ', z,' ,вы вошли в систему!' ,sep='')
        else:
            print('Пароль не верный!')
            k=input('Введите пароль повторно:')
            if a == k:
                print('Успешно! ', z,' ,вы вошли в систему!' ,sep='')
            else:
                print('Убедитесь в том ,что вы ввели правильный пароль и перезапустите программу!')
    else:
        print('Вы ввели не правильное имя пользователя, попробуйте снова!')
        t=input('Введите повторно имя пользователя:')
        if z == t:
            k = input('Введите пароль повторно:')
            if a == k:
                print('Успешно! ', z,' ,вы вошли в систему!' ,sep='')
        else:
            print('Убедитесь в том ,что вы ввели правильное имя пользователя и пароль , далее перезапустите программу!')
else:
    print('О-Оу ,ввели пароль неверно,повторите попытку')
