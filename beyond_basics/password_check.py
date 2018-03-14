"""
Simple exercise to work with loops and string formatting
"""
correct_password = '123456'
name = input("Name: ")
surname = input("Surname: ")
password = input("Password: ")

tries = 1
max_tries = 3

while tries < max_tries and password != correct_password:
    error_message = 'Invalid password (%s tries left). Please, try again: ' % (max_tries - tries)

    tries = tries + 1;

    password = input(error_message)

if password == correct_password:
    success_message = 'Welcome %s %s, you are logged in! :)' % (name, surname)

    print(success_message)
else:
    print('Error: You have exceeded the number of tries! :(')