def helloWorld(name):
    print('Hello World!\nHello {0}'.format(name))
    return

def main():
    name = input('What\'s your name? ')
    helloWorld(name)
    return

main()