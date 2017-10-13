import datetime

currentDate = datetime.date.today()

print(currentDate)

print(currentDate.year)
print(currentDate.month)
print(currentDate.day)

#Sendo %A = dia da semana; %d = dia; %B = mês; %b = Mês abrev; %Y Ano 4 digitos
print(currentDate.strftime('Today is %A, %d %B %Y'))

birthday = input('What is your birthday? ')
#Convertendo string em data | Informando o formato em que a data foi inserida
birthday = datetime.datetime.strptime(birthday,"%d/%m/%Y").date()
print("Your birth month is {0}".format(birthday.strftime('%B')))

#Transformando a data novamente em string para alterar seu formato
birthdayConta = str(birthday.month) + '/' + str(birthday.day) + '/' + str(birthday.year)
#Transformando a string novamente em data
birthdayConta = birthday = datetime.datetime.strptime(birthdayConta,"%m/%d/%Y").date()

#Fazendo conta entre datas
years = currentDate - birthdayConta
print(years.days / 365)