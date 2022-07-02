import turtle

window = turtle.Screen()

# Window Settings
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=600, height=600)

# Head Settings
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "up"


turtle.done()
