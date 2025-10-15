from generator.password_logic import create_password

num_characters = 0
prompt = ''

upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

prompt += 'How many characters would you like your password to have? '
prompt += '(Minimun 8 characters) '

print('\n\t--Password generator--')
num_characters = int(input(prompt))

password = create_password(num_characters)

print(f'\nYour new password is: {password}')