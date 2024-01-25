#import libraries
import turtle
import random
import time

#Creating the screen
screen = turtle.Screen()
screen.title("SNAKE GAME")
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("#1d1d1d")

#creating border
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color("red")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.penup()
turtle.hideturtle()

#score
score = 0;
delay = 0.1

#snake
snake = turtle.Turtle()
snake.speed()
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

#food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("square")
fruit.color("white")
fruit.penup()
fruit.goto(30, 30)

old_fruit = []

#scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")

