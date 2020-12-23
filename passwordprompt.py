password = ''
i=0
while password != 'password':
    print("Please enter your password")
    password = input()
    if password != 'password':
        print('\nSorry the password you entered is wrong')
        i = i + 1
    else:
        print("\nCool you are successfully logged in")
    if i == 3:
        print('You ran out of your attempts')
        break
