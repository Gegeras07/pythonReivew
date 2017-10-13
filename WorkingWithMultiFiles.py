#Para utilizar comandos de prompt do sistema
import os
#Para utilizar recursos do tratamento de exceção
import sys
#Para utilizar recursos da listagem de arquivos do diretório
from os import listdir
from os.path import isfile, join

os.system('clear')

directory = 'pythonCourseMVA/filesTxt/'

while True:

    print('==============================')
    print('=========== Files ============')
    print('==============================\n\n')

    try:
        opt = int(input('1. Create a file .txt\n2. Create a file .csv\n3. Read a file .txt\n4. Read a file .csv\n5. Exit\nChoose a option: '))
    except:
        opt = -1        

    if opt == 1:
        os.system('clear')        
        fileName = input('Choose a file name: ')
        path = directory + fileName + '.txt'
        WRITE = 'w'
        
        try: 
            myFile = open(path, mode = WRITE)

            contentFile = input('Write your text or \'DONE\' to exit: ')

            while contentFile.upper() != 'DONE':
                myFile.write(contentFile + '\n')
                contentFile = input('Write your text or \'DONE\' to exit: ')

            myFile.close()
        #Tratamento de exceção específico
        except IOError as e:
            print('I/O error ({0}): {1}'.format(e.errno, e.strerror))
        #Tratamento de erro para comportamentos inesperados
        except:
            os.system('clear')
            print(sys.exc_info())

    if opt == 3:
        try:
            os.system('clear')
            #Cria uma lista com os arquivos que existem no diretório
            onlyFiles = [f for f in listdir(directory) if isfile(join(directory, f))]

            if len(onlyFiles) != 0:
                #Exibe os arquivos que existem no diretório
                for f in onlyFiles:
                    print(f)

                fileToView = input('Choose the name\'s file: ')

                try:
                    os.system('clear')
                    path = directory + fileToView + '.txt'
                    file = open(path)
                    fileContent = file.read()
                    print(fileContent)
                    file.close()
                except FileNotFoundError:
                    print('File not found.')
                except:
                    print(sys.exc_info())
            else:
                os.system('clear')
                print('The directory is empty!')                
        except:
            os.system('clear')
            print(sys.exc_info())

    elif opt == 5:
        os.system('clear')
        print('End program!')
        break
    else:
        os.system('clear')
        print('--- Wrong option ---')
        if opt == -1:
            print('--- Enter numbers! ---')