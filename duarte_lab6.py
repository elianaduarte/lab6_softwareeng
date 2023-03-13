# Eliana Duarte Lab 6 Software Engineering

def encode(password):
    encpass = ''
    for char in password:
        char = int(char)+3
        encpass = encpass + str(char)
    return encpass

quit = False
menu = 'Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n'
newpass = ''
while not quit:
    print(menu)
    opt = int(input('Please enter an option: '))
    if opt == 1:
        password = input('Please enter your password to encode: ')
        password = encode(password)
        print('Your password has been encoded and stored!')
    elif opt == 2:
        newpass = decode(password)
        print(f'The encoded password is {password}, and the original password is {newpass}.\n')
    elif opt == 3:
        quit = True