table = int(input('Choose the table: '))

for t in range(1,11):
    r = int(input("What is {0} x {1} ? ".format(table, t)))
    while r != table * t:
        print('Wrong!')
        r = int(input("What is {0} x {1} ? ".format(table, t)))