import datetime

currentDate = datetime.datetime.today()
currentTime = datetime.datetime.now()

#Adiciona 15 dias a data atual
print(currentDate + datetime.timedelta(days=15))
#Adiciona 15 horas a data atual
print(currentDate + datetime.timedelta(hours=15))

print(currentTime.hour)
print(currentTime.minute)
print(currentTime.second)

#Formatação de horários
#Formato 24H
print(datetime.datetime.strftime(currentTime,'%H:%M'))
#Formato 12H
print(datetime.datetime.strftime(currentTime,'%I:%M %p'))