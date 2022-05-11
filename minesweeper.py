import random
import tools
import time
class Neural_Network():
    def __init__(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i
        self.j = j
        self.k = k
        self.l = l
        self.m = m
        self.n = n
        self.o = o
        self.p = p
        print(self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h, self.i, self.j, self.k, self.l, self.m, self.n, self.o, self.p)
    def Decide(self, x, y, w, h):
        if x == 0: SL = 0
        else:
            SL = x*self.a + y*self.e + (w-x)*self.i + (h-y)*self.m
        if x == w: SR = 0
        else:
            SR = x*self.b + y*self.f + (w-x)*self.j + (h-y)*self.n
        if y == h: SU = 0
        else:
            SU = x*self.c + y*self.g + (w-x)*self.k + (h-y)*self.o
        if y == 0: SD = 0
        else:
            SD = x*self.d + y*self.h + (w-x)*self.l + (h-y)*self.p
        weights = [SL,SR,SU,SD]
        D = weights[0]
        index = 0
        for w in range(0, len(weights)):
            if weights[w] > D:
                D = weights[w]
                index = w
        return index #0:left,1:right,2:up,3:down

class Player():
    def __init__(self, x, y, max_x, max_y):
        self.x = x
        self.y = y
        self.max_x = max_x
        self.max_y = max_y
    def move(self, x, y):
        if self.x + x > self.max_x or self.x + x < 0:
            return False
        if self.y + y > self.max_y or self.y + y < 0:
            return False
        self.x = self.x + x
        self.y = self.y + y
        return True
    def is_alive(self, minefield):
        for mine in minefield:
            if mine.x == self.x and mine.y == self.y:
                print("Player Dead.")
                return False
        return True
class Mine():
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Field():
    def __init__(self, width, height, mines):
        self.width = width
        self.height = height
        self.mines = mines
    def plant_mines(self):
        minefield = []
        for i in range(0, self.mines):
            minefield.append(len(minefield))
            minefield[len(minefield) - 1] = Mine(random.randint(1, self.width), random.randint(1, self.height))
        return minefield
f = Field(10,10,9)
p = Player(0,0,f.width,f.height)
minefield = f.plant_mines()
n = Neural_Network(tools.randomize(), tools.randomize(), tools.randomize(), tools.randomize(), tools.randomize(), tools.randomize(), tools.randomize(), tools.randomize(), tools.randomize(), tools.randomize(), tools.randomize(), tools.randomize(), tools.randomize(), tools.randomize(), tools.randomize(), tools.randomize())
def Game(f,p,minefield,n):
    rounds = 0
    while True:
        D = n.Decide(p.x,p.y,f.width,f.height) #0:left,1:right,2:up,3:down
        if D == 0:
            p.move(-1,0)
            spawn_mine = Mine(p.x + 1, p.y)
        if D == 1:
            p.move(1,0)
            spawn_mine = Mine(p.x - 1, p.y)
        if D == 2:
            p.move(0,1)
            spawn_mine = Mine(p.x, p.y - 1)
        if D == 3:
            p.move(0,-1)
            spawn_mine = Mine(p.x, p.y + 1)
        minefield.append(len(minefield))
        minefield[len(minefield) - 1] = spawn_mine
        if p.is_alive(minefield) == False:
            print("Game over: " + str(rounds) + ' Rounds.')
            break
        else:
            rounds += 1
        time.sleep(1)
        print("Player position: " + str(p.x) + ':' + str(p.y))
        for mine in minefield:
            print("Mine position: " + str(mine.x) + ':' + str(mine.y))
Game(f,p,minefield,n)
