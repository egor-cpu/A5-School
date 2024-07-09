log_l = []

def reg():
    log = input('Придумайте логин:\n')
    pas = input('Придумайте пароль:\n')
    f = False
    if len(log_l) > 0:
        for i in range(len(log_l)):
            if log_l[i][0] == log:
                f = True
    if f:
        print('Логин занят, придумайте другой')
        reg()
        return
    log_l.append([log, pas])
    print('Вы успешно зарегистрировались!')

def log_in():
    if len(log_l) == 0:
        print('Зарегестрированных пользователей нет, сперва зарестрируйтесь')
        reg()
        return
    log = input('Введите логин:\n')
    pas = input('Введите пароль:\n')
    f = False
    for i in range(len(log_l)):
        if [log, pas] == log_l[i]:
            f = True
    if f:
        print('Вы успешно вошли!')
    else:
        print('Неверный логин или пароль, попробуйте ещё раз')
        log_in()
#Примечание: программа ничего не делает т. к. функции не вызываются