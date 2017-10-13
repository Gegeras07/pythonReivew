import turtle

#Quadrados dentro de um quadrado
#for steps in range(4):
#    turtle.forward(100)
#    turtle.right(90)
#    for moresteps in range(4):
#        turtle.forward(50)
#        turtle.right(90)

#Desenha uma estrela
#for steps in range(5):
#    turtle.forward(100)
#    turtle.right(360/5)
#    for moresteps in range(5):
#        turtle.forward(50)
#        turtle.right(360/5)

#Desenha uma forma de acordo com o número de lados informado
nbrSides = int(input('Enter a number of sides( > 3 ): '))

if(nbrSides < 3):
    print('Impossible to draw an image!')
else:    
    for steps in range(nbrSides):        
        turtle.forward(100)
        turtle.right(360/nbrSides)
    
    #Segura a tela
    turtle.getscreen()._root.mainloop()
    


