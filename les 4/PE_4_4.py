def new_password():
    oldpassword=input('Vul hier je oude wachtwoord in: ')
    newpassword=input('Vul hier je nieuwe wachtwoord in: ')
    if oldpassword != newpassword:
        if len(newpassword)>=6:
            print('True')
    else:
        print('False')
new_password()