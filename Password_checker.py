import re


print('your password must contain: \n-at least 8 letters \n-numbers \n-$,%,$,@')


while True:

    password = input('create your password: ')
    pattern = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[$%@#])[A-Za-z\d$%@#]{8,}$')

    if pattern.search(password) == None:
        print('invalid password, try again')
    else:
        print('password created')
        break

