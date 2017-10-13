import glob, os

directory = 'pythonCourseMVA/filesTxt/'
os.chdir(directory)

cont = 0

for file in glob.glob("*.csv"):
    print(file)
    cont += 1

if cont == 0:
    print('There are no files to view!')