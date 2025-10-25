from generator.password_logic import create_password
from utils.validation import is_Correct

num_characters = 0
answer = ''
prompt = ''

prompt += '\nHow many characters would you like your password to have? '
prompt += '\n(Minimun 8 characters): '

while True:
    print('\n\t--Password generator--')

    try:
        while True:
            num_characters = int(input(prompt))
            
            if num_characters >= 8:
                break
            
            print('\n\tNot enough characters typed!')
            continue
        
    except ValueError:
        print('\nInvalid input. Enter a valid number!')

    else:
        while True:
            password = create_password(num_characters)

            # Check if the password has at least one upper letter, one lower letter,
            # a number and a special character
            if is_Correct(password):
                break

        print(f'\n\t*Your new password is: {password}')

    answer = input('\nWould you like to create another password?'
                   "\nEnter 'quit' if you don't want: ")
    
    if (answer.lower()).strip() == 'quit':
        break