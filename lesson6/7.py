# def create_user(username, isAdmin, resetPassword):
#     pass
#
# create_user("alex99", True, False)

def create_user(username, *,  isAdmin=False, resetPassword=False):
    """выводит информацию о пользователе

    :param username: имя пользователя
    :param isAdmin: свы
    :param resetPassword:сывсыв
    :return: None
    """
    print(username, isAdmin, resetPassword, sep="-", end='!!')
    pass

# create_user("alex99", isAdmin=True, resetPassword=False)

help(create_user)
