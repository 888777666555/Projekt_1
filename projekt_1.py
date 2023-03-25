

"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: David Cudejko
email: david.cudejko@gmail.com
discord: #3576
"""


from task_template import TEXTS

# vstupni udaje
print('$ python projekt1.py')

user_and_password = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'

}

#Vyžádá si od uživatele přihlašovací jméno a heslo
user_name = input('username: ')
user_password = input('password: ')
line = '-' * 55
print(line)

#overeni udaju registrovaných uživatelů,pridal jsem upozorneni kdyz je user ok ale spatne heslo

if user_name  in user_and_password.keys()  and user_password in user_and_password.values():
    print(f'Welcome to the app, {user_name}')
elif user_name  in user_and_password.keys()  and user_password is not user_and_password.values():
    print(f'{user_name} you put wrong password')
    quit()
else:
    print(f' {user_name} is unregistered user, terminating the program.')
    quit()

print('We have 3 texts to be analyzed.')
print(line)

#vyber uzivatele mezi třemi texty a zobrazeni textu dle vyberu

user_text_select = int(input('Enter a number btw. 1 and 3 to select: '))


texts_copy = TEXTS.copy() #kopie textu ze task_template.py
user_choice_extract = '' #vyber uzivatele


if user_text_select == 1:
    user_choice_extract = texts_copy[0]    
elif user_text_select == 2:
    user_choice_extract = texts_copy[1]    
elif user_text_select == 3:
    user_choice_extract = texts_copy[2]    
else:
    print(f'Attention, the entered character {user_choice_extract} does not exist, it must be a number from 1 to 3.')


print(line)

# statistiky

#pocet slov
clean_words = [] # vycistene slova
for words in user_choice_extract.split():
    clean_word = words.strip('.:!?,')
    clean_words.append(clean_word)
print(f'There are {len(clean_words)} words in the selected text.')


#pocet titlecase,uppercase,titlecase words and numeric strings.
lower_case = 0
upper_case = 0
title_case = 0
numeric_case = 0
sum_of_numbers = 0

for i in clean_words:
    if(i.islower()):
        lower_case +=1        
    elif (i.istitle()):
        title_case +=1    
    elif(i.isupper()):
        upper_case +=1
    elif(i.isnumeric()):
        numeric_case +=1

# sum vsech cisel v textu

for x in user_choice_extract.split():
    if (x.isnumeric()) == True:
        z = int(x)
        sum_of_numbers = sum_of_numbers +z
        
print(f"There are {title_case} titlecase words.") 
print(f"There are {upper_case} uppercase words.")
print(f"There are {lower_case} lowercase words.")
print(f"There are {numeric_case} numeric strings.")
print(f"The sum of all the numbers {sum_of_numbers}.")

#graf - četnost různých délek slov v textu  

lenght_of_words = []

for y in clean_words:
    lenght=len(y) 
    lenght_of_words.append(lenght)

frequency = {}

for item in lenght_of_words:
    if item in frequency:
        frequency[item] +=1
    else:
        frequency[item] = 1
print(line)


# delka slova a pocet slov
print("{:<15}  {:<15}".format('LEN', 'OCCURENCES'),'NR')

for key, value in frequency.items():
    len_1 = key
    o = '*' * key
    nr = value
    
    print("{:<15} {:<15} {:<15}".format(len_1, o, nr))






        

    













