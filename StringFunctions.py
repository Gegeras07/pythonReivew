message = 'Hello World'

#Torna todas as letras minúsculas
print(message.lower())
#Torna todas as letras maiúsculas
print(message.upper())
#Inverte a captalização das letras
print(message.swapcase())
#Procura uma cadeia específica de caracteres numa string; retorna -1 se não encontrar
print(message.find('World'))
#Procura uma cadeia específica de caracteres numa string e retorna o número de ocorrências
print(message.count('o'))
#Deixa a primeira letras maiúscula e as demais minúsculas
message = message.lower()
print(message.capitalize())
#Troca uma ocorrência de caracteres por outra
print(message.replace('hello','Hi'))