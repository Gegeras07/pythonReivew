import datetime

country = input('Where are you from? ')
language = input('What is your language? ')
currentDate = datetime.datetime.today()

#Operador E
if country.upper() == 'CANADA' and language.upper() == 'ENGLISH':
    print('Hello')
elif country.upper() == 'GERMANY' and language.upper() == 'GERMAN':
    print('Guten Tag')
elif country.upper() == 'FRANCE' and language.upper() == 'FRANCH':
    print('Bonjour')
else:
    print('Eh nois!')

#Operador OU
week = currentDate.strftime('%A')
hora = currentDate.hour
print (hora)

if week.upper() == 'TUESDAY' or 'MONDAY':
    print('Let\'s work hard!')
    if hora < 8 and hora > 18:
        print('No work')
    elif hora >= 12 and hora < 13:
        print('Lunch time!')
    elif hora > 17:
        print('Almost go out!')
    else:
        print('WOOOOOOOOORK!')    
else:
    print('SLEEEEEEEEEEEEEEEP!')
    