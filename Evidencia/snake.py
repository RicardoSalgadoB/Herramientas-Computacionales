"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange, choice
from turtle import *

from freegames import square, vector

# Ricardo Salgado - A01282489
colors = ['green', 'red', 'blue']
color_superpower = {
    'green': 'Fruta Normal',
    'red':'Fruta de Crecimiento',
    'blue':'Fruta de Invulnerabilidad'
}
not_popping = 0
invulnerability = 0
food_color = 'green'

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    """Move snake forward one segment."""
    # Ricardo Salgado - A01282489
    global food_color, not_popping, invulnerability
    
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        if invulnerability == 0:
            square(head.x, head.y, 9, 'red')
            update()
            return
        else:
            if -200 > head.x:
                head.x += 380
            elif head.x > 190:
                head.x -= 380
                
            if -200 > head.y:
                head.y += 380
            elif head.y > 190:
                head.y -= 380

    snake.append(head)

    # Ricardo Salgado - A01282489
    if invulnerability == 1:
        print("Se terminó la invulnerabilidad")
    if invulnerability > 0:
        invulnerability -= 1
    
    if head == food:
        # Ricardo Salgado - A01282489
        # Efectos
        if food_color == 'red': # Aumentar tamño x5
            not_popping = 5
        elif food_color == 'blue':  # Invulnerabilidad por 35 turnos
            invulnerability = 35
            not_popping = 1
        else:
            not_popping = 1
        
        # Mostrar superpoder de la fruta
        print(color_superpower[food_color])
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        food_color = choice(colors)
    
    # Ricardo Salagdo - A01282489
    if not_popping == 0:
        snake.pop(0)
    else:
        not_popping -= 1

    clear()
    
    # Ricardo Salgado - A01282489
    for i in range(-23, 22):
        for j in range(-23, 22):
            if (j+i)%2 == 0:
                square(j*10, i*10, 9, 'gray')
            else:
                square(j*10, i*10, 9, 'white')

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, food_color)
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
