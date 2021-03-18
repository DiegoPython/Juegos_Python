from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
found_pairs = 0

class Contador(object):

  def __init__(self, inicial=0):
    self.numero = inicial

  def siguiente(self):
    self.numero += 1
    return self.numero

conttap = Contador()

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']
    global found_pairs

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        found_pairs = found_pairs + 1
    
    up()
    goto(200,200)
    color('red')
    write(conttap.siguiente(), font=('Arial', 30, 'normal'))

def draw():
    print(found_pairs)
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        #Reposicionamos nuestro texto
        goto(x + 25, y)
        write(tiles[mark], align='center', font=('Arial', 30, 'normal'))

    if found_pairs == 32:
        goto(0, 0)
        color('blue')
        write('Felicidades, encontraste todas las parejas!', align='center', font=('Arial', 14, 'normal'))


    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()