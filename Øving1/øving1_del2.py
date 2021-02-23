# oppgåve 1e)
import turtle
vinkel=int(input("Velg vinkel: "))
ganger=int(360/vinkel)
for tall in range(1,ganger+1):
    turtle.forward(50)
    turtle.back(50)
    turtle.left(vinkel)
turtle.done()


