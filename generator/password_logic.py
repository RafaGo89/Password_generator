import random
from generator.config import upper_letters
from generator.config import lower_letters
from generator.config import special_characters

def create_password(min_characters):
    """Generates a password of a given length"""
    password = ''
    
    while min_characters != 0:
        min_characters -= 1
        
        # Generating a random number from 1 to 4
        random_choice = random.randint(1, 4)
        
        match random_choice:
            case 1:
                password += random_uppper()
            case 2:
                password += random_lower()
            case 3:
                password += str(random.randint(0, 9))
            case 4:
                password += random_special_character()
            case _:
                pass
            
    return password

def random_uppper():
    """Picks a random upper letter"""
    random_picker = random.randint(0, len(upper_letters) - 1)
    
    letter_chosen = upper_letters[random_picker]
    
    return letter_chosen

def random_lower():
    """Picks a random lower letter"""
    random_picker = random.randint(0, len(lower_letters) - 1)
    
    letter_chosen = lower_letters[random_picker]
    
    return letter_chosen

def random_special_character():
    """Picks a random special character"""
    random_picker = random.randint(0, len(special_characters) - 1)
    
    letter_chosen = special_characters[random_picker]
    
    return letter_chosen