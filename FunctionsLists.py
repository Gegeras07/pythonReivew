#Lists Functions
import os

names = []
points = []

#Permite usar comandos do Terminal (console) do sistema
os.system('clear')

while True:
    try:        
        opt = int(input('1. Add new itens\n2. List new itens\n3. Remove itens\n4. Exit\nEnter option: '))
    except:
        opt = 5      

    if opt == 1:
        os.system('clear')
        #Add a new item
        names.append(input('New name: '))
        points.append(int(input('Points: ')))
        os.system('clear')
        print('--------------------------')
        print('Guy add!')
        print('--------------------------\n\n')
    elif opt == 2:
        if(len(names) == 0):
            os.system('clear')
            print('----------------------------------')
            print('There are no elements to show!')
            print('----------------------------------\n\n')
        else:
            os.system('clear')
            print('----------------------------------')
            for l in range(len(names)):
                print("Name: {0} = {1}".format(names[l], points[l]))

            print('----------------------------------\n\n')
    elif opt == 3:
        position = -1
        if(len(names) == 0):
            os.system('clear')
            print('-------------------------------------')
            print('There are no elements to remove!')
            print('----------------------------------\n\n')
        else:
            os.system('clear')            
            name = input('Which name do you want to remove? ')
            
            try:
                #index(x) = procura um item qualquer e retorna sua posição; 
                #retorna um erro se o item informado ñ existir
                position = names.index(name)
            except:
                os.system('clear')
                position = -1
                print('The name informed does not exist')               
                
            if position != -1:
                os.system('clear')
                print('-------------------------------------')
                #pop(i) = Remove o item na posição i e o retorna
                print("{0} was removed.".format(names.pop(position)))
                print('-------------------------------------\n\n')
                #remove(x) = Remove o item de valor 'x' da lista
                points.remove(points[position])
    elif opt == 4:
        os.system('clear')
        break
    else:
        os.system('clear')
        print('-------------------------------------')
        print('Wrong option!')
        if opt == 5:
            print('Do not use letters!')
        print('-------------------------------------\n\n')

print('End of the program!')                