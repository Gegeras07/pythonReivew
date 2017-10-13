print('Hello world!')
name = input('What\'s your name? ')
print("Hello {0}".format(name.capitalize()))

option = input('Write \'yes\' or \'no\': ')

if option.lower() == 'yes':
    print('Go ahead my friend!')
else:
    print('Bye :\'(')
    