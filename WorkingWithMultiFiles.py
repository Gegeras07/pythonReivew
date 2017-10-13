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
        directoryLocal = directory + '/filesTxt/'
        #Define o diretório a ser utilizado
        os.chdir(directoryLocal)        
        fileName = input('Choose a file name: ')
        path = directoryLocal + fileName + '.txt'        
        
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

    elif opt == 2:
        os.system('clear')
        directoryLocal = directory + '/filesCsv/'
        #Define o diretório a ser utilizado
        os.chdir(directoryLocal)        
        fileName = input('Choose a file name: ')
        path = directoryLocal + fileName + '.csv'        
        
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

    elif opt == 3:
        os.system('clear')
        directoryLocal = directory + '/filesTxt/'
        os.chdir(directoryLocal)
        cont = 0

        #Lista os arquivos de acordo com o diretório e a extensão selecionadas
        for file in glob.glob("*.txt"):
            print(file)
            cont += 1

        if cont != 0:            
            
            fileToView = input('Choose the name\'s file: ')

            try:
                os.system('clear')
                path = directoryLocal + fileToView + '.txt'
                myFile = open(path, mode = READ)
                fileContent = myFile.read()
                print(fileContent)
                myFile.close()
            except IOError as e:
                print('I/O error ({0}): {1}'.format(e.errno, e.strerror))
            except:
                os.system('clear')
                print(sys.exc_info())            
                
        else:
            print('There are no files to view!')       

    elif opt == 4:
        os.system('clear')
        directoryLocal = directory + '/filesCsv/'
        os.chdir(directoryLocal)
        cont = 0

        #Lista os arquivos de acordo com o diretório e a extensão selecionadas
        for file in glob.glob("*.csv"):
            print(file)
            cont += 1

        if cont != 0:            
            
            fileToView = input('Choose the name\'s file: ')            

            try:
                os.system('clear')
                delimiterCh = input('Choose the delimiter character: ')
                path = directoryLocal + fileToView + '.csv'
                
                with open(path, READ) as myCsvFile:
                    #Read the file contents | Specifies the delimiter
                    dataFromFile = csv.reader(myCsvFile, delimiter=delimiterCh)

                    #For loop that will run once per row
                    for row in dataFromFile:
                        print(row)
               
            except IOError as e:
                print('I/O error ({0}): {1}'.format(e.errno, e.strerror))
            except:
                os.system('clear')
                print(sys.exc_info())            
                
        else:
            print('There are no files to view!')

    elif opt == 5:
        os.system('clear')
        print('End program!')
        break
    else:
        os.system('clear')
        print('--- Wrong option ---')
        if opt == -1:
            print('--- Enter numbers! ---')