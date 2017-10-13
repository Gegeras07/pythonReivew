import turtle

for steps in ['red', 'blue' ,'green', 'black']:
    turtle.color(steps)
    turtle.forward(100)
    turtle.right(90)

#Segura a tela
turtle.getscreen()._root.mainloop()