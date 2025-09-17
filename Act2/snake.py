"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *

from freegames import square, vector


from random import randrange, choice

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

"""Leonardo Orozco A00843030:
A las propiedades se le agrega una nueva:"""
obstacle = vector(1000 ,1000)

# Irasema Álvarez Treviño - A01286449
colors = ['blue', 'green', 'purple', 'orange', 'pink']
snake_color = choice(colors)
food_color = choice(colors)

# Juan Antonio Rodríguez Reyna - A01571918
speed = 100  

# Irasema Álvarez Treviño - A01286449
while food_color == snake_color:
    food_color = choice(colors)

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    global speed
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return
    
    # Leonardo Orozco -  A00843030
    if not inside(head) or head in snake or (head.x == obstacle.x and head.y == obstacle.y):
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        # Juan Antonio Rodríguez Reyna - A01571918
        speed = max(20, speed - 5)   # pyright: ignore[reportOperatorIssue]
    else:
        # Ricardo Salgado Benítez - A01282489
        delta_x = randrange(-1, 2) * 10
        delta_y = randrange(-1, 2) * 10
        if -200 < food.x + delta_x < 190 and -200 < food.y + delta_y < 190:
            food.x += delta_x
            food.y += delta_y
        
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    square(obstacle.x, obstacle.y, 9, 'black')

    update()
    ontimer(move, 100)



"""Leonardo Orozco A00843030:
Con esto se posiciona el obstaculo dentro del area de juego y cambia de posicion cada 5 segundos,
ademas de que el mismo obstaculo no aparece con la fruta nunca"""
def mover_obstaculo():  
    while True:
        pos = vector(randrange(-15,15) *10 ,randrange(-15,15)*10)
        if pos not in snake and pos != food:
            obstacle.x, obstacle.y = pos.x, pos.y
            break

    ontimer(mover_obstaculo, 5000)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
mover_obstaculo()
done()
