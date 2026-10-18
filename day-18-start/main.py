# from turtle import Turtle, Screen
import turtle as t
import random

timmy_the_turtle = t.Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# for _ in range(4):
#   timmy_the_turtle.forward(100)
#   timmy_the_turtle.left(90)

# for _ in range(20):
#   timmy_the_turtle.pendown()
#   timmy_the_turtle.forward(5)
#   timmy_the_turtle.penup()
#   timmy_the_turtle.forward(5)


# colors = ["red", "green", "blue", "yellow", "cyan", "magenta"]

# def draw_shape(num_sides):
#   angle =  360 / num_sides
#   for _ in range(num_sides):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(angle)

# for shape_sides_n in range(3, 11):
#   timmy_the_turtle.color(random.choice(colors))
#   draw_shape(shape_sides_n)

t.colormode(255)

def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  random_color = (r, g, b)
  return random_color

directions = [0, 90, 180, 270]

timmy_the_turtle.speed("fastest")

# for _ in range(200):
#   timmy_the_turtle.color(random_color())
#   timmy_the_turtle.forward(30)
#   timmy_the_turtle.setheading(random.choice(directions))

def draw_a_spirograph(size_of_gap):
  for _ in range(int(360 / size_of_gap)):
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.circle(100)
    timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)


draw_a_spirograph(5)

screen = t.Screen()
screen.exitonclick()