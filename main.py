from turtle import Turtle, Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,  "Down")
screen.onkey(snake.left,  "Left")
screen.onkey(snake.right,  "Right")



game_is_on = True
score = 0
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect Collition with food
    if snake.segments[0].distance(food)< 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    #Detect Collision with wall
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    #Detect Tail Collisoin
    for i in snake.segments[1:]:
        if snake.segments[0].distance(i) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
