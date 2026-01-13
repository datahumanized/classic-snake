from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('#D9E231')
screen.tracer(0)

screen.setup(width= 620, height= 620)
# root = screen.cv._rootwindow
# root.resizable(False, False)
screen.title("Classic Snake Game ")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up,'Up',)
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.segments[0].distance(food)< 15:
        food.refresh()
        score.increase_score()
        snake.extend_snake()
    # If you want the  snake to go through the wall and come on the other side
    # Detect if the snake goes beyond the wall
    # Horizontal wall
    if snake.segments[0].xcor() > 300:
        y = snake.segments[0].ycor()
        snake.segments[0].setpos(-300,y)
    if snake.segments[0].xcor() < - 300:
        y = snake.segments[0].ycor()
        snake.segments[0].setpos(300,y)

    # for vertical wall
    if snake.segments[0].ycor() > 300:
        x = snake.segments[0].xcor()
        snake.segments[0].setpos(x,-300)
    if snake.segments[0].ycor() < - 300:
        x = snake.segments[0].xcor()
        snake.segments[0].setpos(x, 300)

    # # If You want to end the game on wall collision
    # if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or  snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280 :
    #     game_is_on = False
    #     score.goto(0, 0)
    #     score.color('DarkSlateBlue')
    #     score.write(f"Game Over!", align="center", font=("courier", 24, 'bold'))
    # Self collision
    for seg in snake.segments[1:]:
        if snake.segments[0].distance(seg) < 10:
            game_is_on = False
            score.game_over()
            score.reset_score()





screen.exitonclick()