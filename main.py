from generator.password_logic import create_password
from utils.validation import is_Correct

num_characters = 0
prompt = ''

prompt += '\nHow many characters would you like your password to have? '
prompt += '\n(Minimun 8 characters): '

print('\n\t--Password generator--')

while True:
    num_characters = int(input(prompt))
    
    if num_characters >= 8:
        break
    
    print('\n\tNot enough characters typed!')
    continue
    
while True:
    password = create_password(num_characters)

    # Check if the password has at least one upper letter, one lower letter,
    # a number and a special character
    if is_Correct(password):
        break

print(f'\n\t*Your new password is: {password}')