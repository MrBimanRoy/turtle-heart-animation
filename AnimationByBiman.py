import turtle
import time

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Animated Heart 💖")

heart = turtle.Turtle()
heart.pensize(3)
heart.speed(1)
heart.color("red", "pink")

def draw_heart():
    heart.begin_fill()
    heart.left(140)
    heart.forward(180)
    heart.circle(-90, 200)
    heart.setheading(60)
    heart.circle(-90, 200)
    heart.forward(180)
    heart.end_fill()

draw_heart()

# Display a text message
heart.penup()
heart.goto(0, -180)
heart.color("black")
heart.write("With Love ❤️ - Biman", align="center", font=("Arial", 16, "bold"))

# Hide the turtle
heart.hideturtle()

# Keep window open
turtle.done()
