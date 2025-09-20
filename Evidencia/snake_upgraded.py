from random import randrange, choice
from turtle import *
from turtle import Terminator
from freegames import square, vector

# Ricardo Salgado - A01282489
colors = ['green', 'red', 'blue']  # se ampliará dinámicamente abajo- Leonardo Orozco A00843030
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
# Juan Antonio Rdz. - A01571918
velocidad = 10

# Irasema Alvarez - A01286449
available_colors = ['light gray', 'orange', 'purple', 'brown', 'steel blue', 'magenta']
background_color = choice(available_colors)
snake_color = choice(available_colors)

while snake_color == background_color:
    snake_color = choice(available_colors)

obstacles = []

#nuevos estados/limites Leonardo Orozco A00843030
left_bound, right_bound = -200, 190
bottom_bound, top_bound = -200, 190

# muros centrales (aparecen/desaparecen tras fruta amarilla)
walls = []
walls_active = False

# obstaculos móviles (fruta morada) + congelación (fruta cyan)
mobs = []
mobs_freeze = 0

# habilitar frutas especiales
colors = ['green', 'red', 'blue', 'yellow', 'purple', 'cyan']
color_superpower.update({
    'yellow': 'Muros Centrales ON/OFF',
    'purple': 'Obstáculos Móviles',
    'cyan': 'Congelar Obstáculos Móviles',
})

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    # Usar límites variables)Leonardo Orozco A00843030
    return left_bound < head.x < right_bound and bottom_bound < head.y < top_bound

def build_central_walls():
    # Leonardo Orozco A00843030
    global walls
    walls = []
    # cruz centrada
    for dx in range(-15, 16):
        v = vector(dx*10, 0)
        if v not in walls:
            walls.append(v)
    for dy in range(-15, 16):
        v = vector(0, dy*10)
        if v not in walls:
            walls.append(v)

def toggle_walls():
    #Leonardo Orozco A00843030
    global walls_active
    if walls_active:
        walls.clear()
        walls_active = False
    else:
        build_central_walls()
        walls_active = True

def spawn_mobs(n=3):
    #Leonardo Orozco A00843030
    from random import shuffle
    dirs = [vector(10,0), vector(-10,0), vector(0,10), vector(0,-10)]
    created = 0
    attempts = 0
    while created < n and attempts < 200:
        attempts += 1
        p = vector(randrange(-15,15)*10, randrange(-15,15)*10)
        if (p not in snake and p != food and p not in obstacles and p not in walls
            and all(p != m['pos'] for m in mobs)):
            d = choice(dirs)
            mobs.append({'pos': p, 'dir': d})
            created += 1

def move_mobs():
    #Leonardo Orozco A00843030
    global mobs_freeze
    if mobs_freeze > 0:
        mobs_freeze -= 1
        return
    for m in mobs:
        nxt = m['pos'].copy()
        nxt.move(m['dir'])
        # rebote en muros
        if (not inside(nxt)) or (nxt in walls) or (nxt in obstacles):
            m['dir'].x = -m['dir'].x
            m['dir'].y = -m['dir'].y
            nxt = m['pos'].copy()
            nxt.move(m['dir'])
        m['pos'] = nxt

def increase_map():
    #Leonardo Orozco A00843030
    global left_bound, right_bound, bottom_bound, top_bound
    left_bound  -= 40
    right_bound += 40
    bottom_bound -= 40
    top_bound   += 40


def move():
    """Move snake forward one segment."""
    # Ricardo Salgado - A01282489
    global food_color, not_popping, invulnerability, velocidad
    
    #Move a los malos antes de cualquier choque- Leonardo Orozco A00843030
    move_mobs()

    head = snake[-1].copy()
    head.move(aim)

    # Para agregar a los malos sin interrumpir a las frutas Leonardo Orozco A00843030
    hits_border = not inside(head)
    hits_snake_or_static = head in snake or head in obstacles or head in walls
    hits_mob = any(head == m['pos'] for m in mobs)
    if (head != food) and (hits_border or hits_snake_or_static or hits_mob):
        if invulnerability == 0:
            square(head.x, head.y, 9, 'red')
            update()
            return
        else:
            if left_bound > head.x:
                head.x = right_bound - 10
            elif head.x > right_bound - 10:
                head.x = left_bound
            if bottom_bound > head.y:
                head.y = top_bound - 10
            elif head.y > top_bound - 10:
                head.y = bottom_bound

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
        # Juan Antonio Rdz. - A01571918
            velocidad = max(20, velocidad - 10) 
        elif food_color == 'blue':  # Invulnerabilidad por 35 turnos
            invulnerability = 35
            not_popping = 1
        # Juan Antonio Rdz. - A01571918
            velocidad += 10
        else:
            not_popping = 1

        #Leonardo Orozco A00843030
        if food_color == 'yellow':
            toggle_walls()
        elif food_color == 'purple':
            spawn_mobs(n=3)
        elif food_color == 'cyan':
            global mobs_freeze
            mobs_freeze = 50

        
        # Mostrar superpoder de la fruta
        print(color_superpower[food_color])
        print('Snake:', len(snake))

        # Leonardo Orozco A00843030
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        while (food in obstacles) or (food in walls) or any(food == m['pos'] for m in mobs):
            food.x = randrange(-15, 15) * 10
            food.y = randrange(-15, 15) * 10

        food_color = choice(colors)

        # Irasema Alvarez - A01286449
        # Generar obstáculo aleatorio
        new_obstacle = vector(randrange(-15, 15) * 10, randrange(-15, 15) * 10)
        # Asegurar que no aparezca encima de la serpiente ni de la fruta
        while (new_obstacle in snake or new_obstacle == food or new_obstacle in obstacles
               or new_obstacle in walls or any(new_obstacle == m['pos'] for m in mobs)):  #Leonardo Orozco A00843030
            new_obstacle = vector(randrange(-15, 15) * 10, randrange(-15, 15) * 10)
        obstacles.append(new_obstacle)
    
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
                square(j*10, i*10, 9, background_color) # Cambio de gray a color aleatorio -Irasema
            else:
                square(j*10, i*10, 9, 'white') 

    for body in snake:
        square(body.x, body.y, 9, snake_color) # De black a color aleatorio -Irasema
    
    square(food.x, food.y, 9, food_color)
    for obs in obstacles:
        square(obs.x, obs.y, 9, 'black')

    # Dibujo de muros y malos-  Leonardo Orozco A00843030
    for w in walls:
        square(w.x, w.y, 9, 'gray25')
    for m in mobs:
        square(m['pos'].x, m['pos'].y, 9, 'dark orange')

    update()
    try:
        ontimer(move, velocidad)
    except Terminator:
        return
    ontimer(move, velocidad) 


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
