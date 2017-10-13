fileName = 'pythonCourseMVA/filesTxt/demo.txt'
READ = 'r'

myFile = open(fileName, mode = READ)
#All file
fileContent = myFile.read()
#Single line
fileContent = myFile.readline()
#Print the content
print(fileContent)