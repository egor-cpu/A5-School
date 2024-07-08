
log_l = []

def reg():
    log = input('Придумайте логин:\n')#, end='\n')
    pas = input('Придумайте пароль:\n')#, end='\n')
    f = False
    if len(log_l) > 0:
        for i in range(len(log_l)):
            if log in log_l[i] and not f:
                f = True
    if f:
        print('Логин занят, попробуйте другой')
        reg(log, pas)
    else:
        log_l.append([log, pas])

def log_in():
    log = input('Введите логин:\n')
    pas = input('Введите пароль:\n')
    f = False
    if len(log_l) == 0:
        print('Зарегестрированных пользователей нет', 'Используйте "reg()" для регистрации', sep='\n')
        return
    for i in range(len(log_l)):
        if log_l[i] == [log, pas]:
            print('Вход успешно выполнен')
            return
        else:
            print('Неверный логин или пароль', 'Попробуйте ещё раз', sep = '\n')
            log_in()
            return

reg()
