from turtle import Screen, Turtle
import time
from Snaker import Snake
from food import Food
from scoreboard import Score_board
screen=Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.title("Snake Game")
screen.tracer(0)
snake=Snake()
food=Food()
scoreboard=Score_board()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    if snake.segments[0].xcor()>290 or snake.segments[0].ycor()>280 or snake.segments[0].xcor()<-290 or snake.segments[0].ycor()<-280:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) <5:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
