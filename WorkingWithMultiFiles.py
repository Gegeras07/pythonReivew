#Para utilizar comandos de prompt do sistema
import os
#Para utilizar recursos do tratamento de exceção
import sys
#Para utilizar recursos de listagem de diretório
import glob
#Para utilizar arquivos csv
import csv

os.system('clear')

directory = '/home/gegeras/Documentos/Python/pythonCourseMVA'

READ = 'r'
WRITE = 'w'

def makeFile(ext):
    os.system('clear')
    fileName = input('Choose de name\'s file: ')

    os.system('clear')
    directoryLocal = directory + '/files' + ext.capitalize() + '/'
    #Define o diretório a ser utilizado
    os.chdir(directoryLocal)   
    path = directoryLocal + fileName + '.' + ext        
    
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
    return

def readFile(ext):
    os.system('clear')
    directoryLocal = directory + '/files' + ext.capitalize() + '/'
    #Define o diretório a ser utilizado
    os.chdir(directoryLocal)
    cont = 0

    #Lista os arquivos de acordo com o diretório e a extensão selecionadas
    for file in glob.glob("*." + ext):
        print(file)
        cont += 1

    if cont != 0:            
            
        fileToView = input('Choose the name\'s file: ')

        try:
            os.system('clear')
            path = directoryLocal + fileToView + '.' + ext

            if ext == 'txt':
                myFile = open(path, mode = READ)
                fileContent = myFile.read()
                print(fileContent)
                myFile.close()
            else:                
                with open(path, READ) as myCsvFile:
                    #Read the file contents | Specifies the delimiter
                    dataFromFile = csv.reader(myCsvFile)

                    #For loop that will run once per row
                    for row in dataFromFile:
                        print(row)
            
        except FileNotFoundError:
            print('File not Found')
        except:
            os.system('clear')
            print(sys.exc_info())            
            
    else:
        print('There are no files to view!')

    return

while True:   

    print('==============================')
    print('=========== Files ============')
    print('==============================\n\n')

    try:
        opt = int(input('1. Create a file .txt\n2. Create a file .csv\n3. Read a file .txt\n4. Read a file .csv\n5. Exit\nChoose a option: '))
    except:
        opt = -1        

    if opt == 1:        
        makeFile('txt')

    elif opt == 2:        
        makeFile('csv')

    elif opt == 3:
        readFile('txt')               

    elif opt == 4:
        readFile('csv')

    elif opt == 5:
        os.system('clear')
        print('End program!')
        break
    else:
        os.system('clear')
        print('--- Wrong option ---')
        if opt == -1:
            print('--- Enter numbers! ---')