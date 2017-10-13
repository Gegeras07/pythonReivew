print('Playing with numbers')

num = int(input('Enter a number or -1 to exit: '))
sum = 0
cont = 0

while num != -1:
    sum += num
    cont += 1
    num = float(input('Enter a number or -1 to exit: '))

if cont != 0:
    average = sum / cont
    print("The average of {0:d} inserted numbers is {1:.2f}".format(cont,average))
else:
        print('There are no number to show.')

# int(value) -> Converte valores para inteiro
# long(value) -> Converte valore para inteiros longos
# float(value) -> Converte valores para ponto flutuante
# str(value) -> Converte para string