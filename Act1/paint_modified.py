"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""
from math import sqrt

from turtle import *

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Draws circle.
    
    - The diameter is given by whichever of the following is bigger:
        - x coordinate difference of start and end
        - y coordinate difference of start and end
    """
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # 180 times the cursor turns 2°, meaning a 360° circle
    for count in range(180):
        # Divided by 57, because 180/pi ≈ 57
        forward(max(abs(end.x - start.x), abs(end.y - start.y))/57)
        
        # Make sure the circle goes upward or downward, depending on whether end is below start
        if end.y < start.y:
            right(2)
        else:
            left(2)

    end_fill()


def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    width = end.x - start.x
    height = end.y - start.y

    for count in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)

    end_fill()


def triangle(start, end):
    """Se creara el triangulo utilizando de base la longitud entre el primer y segundo click."""
    side = end.x - start.x
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for _ in range(3):
        forward(side)
        left(120)
    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
