# TODO create screen
# TODO create middle line
# TODO create scoreboard: score1 and score2
# TODO create paddle(user) and paddle(computer)
# TODO paddle(user) controlled by user
# TODO paddle (computer) controlled by computer
# TODO create ball, move ball, bounce logic
# TODO detect collisions with wall and paddles
# TODO how do you score? score keeping
# TODO change ball speed


from turtle import Screen
from middle import Middle_Line
#from snake import Snake
#from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

middle = Middle_Line()
scoreboard = Scoreboard()
screen.update()
screen.listen()
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")

# game_is_on = True
#
# while game_is_on:
#     # update screen and wait for 0.05 sec
#     screen.update()
#     time.sleep(0.1)
#
#     #snake.move()
#     # detect collision with food:
#     if snake.head.distance(food) < 15:
#         food.refresh()
#         snake.extend()
#         scoreboard.score += 1
#         scoreboard.update_score(scoreboard.score)
#
#     # detect collision with wall:
#     if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
#         game_is_on = False
#         scoreboard.game_over()
#
#     # detect collision with snake tail
#     for segment in snake.segments[2:]:
#         if snake.head.distance(segment) < 10:
#             game_is_on = False
#             scoreboard.game_over()
#
#
#


#









screen.exitonclick()

