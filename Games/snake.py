import time
import turtle

delay = 0.1
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


def movement():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 10)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 10)

    if head.direction == "right":
        y = head.xcor()
        head.setx(y + 10)

    if head.direction == "left":
        y = head.xcor()
        head.setx(y - 10)


while True:
    window.update()
    movement()
    time.sleep(delay)

turtle.done()
