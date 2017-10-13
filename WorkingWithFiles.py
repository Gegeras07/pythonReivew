#myFile = open(fileName.ext, accessMode)
#accessMode == r (Read the file) | w (Write the file) | a (Append to the existing file content)

fileName = 'pythonCourseMVA/filesTxt/demo.txt'
APPEND = 'a'

myfile = open(fileName, mode = APPEND)

name = input('Write a name or \'DONE\' to exit: ')

while name.upper() != 'DONE':
    myfile.write(name + '\n')
    name = input('Write a name or \'DONE\' to exit: ')

myfile.close()

print('Fim')