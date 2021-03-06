"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""
import random
from random import choice
from turtle import *
from random import randrange
from freegames import square, vector



food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
food_aim = vector(0, 2)


def eaten(head, food):
    "Return True if head is near the food."
    if (food.x - 10) < head.x and head.x < (food.x + 10) and (food.y - 10) < head.y and head.y < (food.y + 10):
        return True
    else:
        return False


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    colors = ['blue','green','yellow','brown','grey']
    # Food aim direction options
    food_aim_options = [
        vector(2, 0),
        vector(-2, 0),
        vector(0, 2),
        vector(0, -2)
    ]

    if head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head) # Add new head to snake

    # Move food in the same direction if its inside the canvas
    if inside(food):
        food.move(food_aim)
    else:
        # Put food in random position
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        # Change its direction
        new_aim = choice(food_aim_options)
        food_aim.x = new_aim.x
        food_aim.y = new_aim.y

    # If food has been eaten
    if eaten(head, food):
        print('Snake:', len(snake))
        # Put food in random position
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        # Change its direction
        new_aim = choice(food_aim_options)
        food_aim.x = new_aim.x
        food_aim.y = new_aim.y
    else:
        snake.pop(0)

    clear()

    # Draw body
    for body in snake:
        square(body.x, body.y, 9, 'black')

    # Change head and food color
    square(head.x, head.y, 9, random.choice(colors))
    square(food.x, food.y, 9, random.choice(colors))

    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
