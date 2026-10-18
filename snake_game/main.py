from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


# x_positions = [-40, -20, 0]
# snake_body = []

# for snake_positions in range(0, 3):
#   turtle = Turtle("square")
#   turtle.color("white")
#   turtle.setpos(x_positions[snake_positions], 0)
#   snake_body.append(turtle)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
  screen.update()
  time.sleep(0.1)
  snake.move()
  
  if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    scoreboard.increase_score()
    
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    scoreboard.reset()
    snake.reset()
    
  for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
      scoreboard.reset()

# segment_1 = Turtle("square")
# segment_1.color("white")


# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20, 0)


# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.goto(-40, 0)


screen.exitonclick()
  