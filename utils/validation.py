from generator.config import upper_letters
from generator.config import lower_letters
from generator.config import special_characters
from generator.config import numbers

def is_Correct(password):
    """Checks if the password has at least one upper, lower, number and
    special charcter"""
    checks = 0
    has_all_characters = False

    # Special characters
    for character in  special_characters:
        if  character in password:
            checks += 1
            break

    # Numbers
    for number in numbers:
        if str(number) in password:
            checks += 1
            break

    # Upper letters
    for letter in upper_letters:
        if letter in password:
            checks += 1
            break

    # Lower letters
    for letter in lower_letters:
        if letter.lower() in password:
            checks += 1
            break

    # Checking if the password has all the characters
    if checks == 4:
        has_all_characters = True
    
    return has_all_characters