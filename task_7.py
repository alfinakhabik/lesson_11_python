def login():
    u = {'alfinakhabik': '2006', 'Max': '0000', 'superman': '9999'}
    log = input('Введите логин: ')
    password = input('Введите пароль: ')
    if log in u:
        if u[log] == password:
            print('Доступ разрешен')
        else:
            print('Доступ запрещен')
    else:
        u[log] = password
        print('Регистрация прошла успешно!')
login()

