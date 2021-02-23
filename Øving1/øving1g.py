# oppgåve 1g
import turtle
antal_stjerner=int(input("Antall stjerner: "))
vinkel=int(input("Velg vinkel: "))
ganger=int(360/vinkel)
turtle.penup()
turtle.backward(75*antal_stjerner)
turtle.pendown()
for x in range(antal_stjerner):
   for tall in range(1,ganger+1):
       turtle.forward(50)
       turtle.back(50)
       turtle.left(vinkel)
   turtle.penup()
   turtle.forward(150)
   turtle.pendown()
turtle.done()
