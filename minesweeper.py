import random
import tools
import time
from numba import jit, cuda
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
        self.track = []
        #print(self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h, self.i, self.j, self.k, self.l, self.m, self.n, self.o, self.p)
    def Decide(self, x, y, w, h):
        if x == 1: SL = 0
        else:
            SL = x*self.a + y*self.e + (w-x)*self.i + (h-y)*self.m
        if x == w: SR = 0
        else:
            SR = x*self.b + y*self.f + (w-x)*self.j + (h-y)*self.n
        if y == h: SU = 0
        else:
            SU = x*self.c + y*self.g + (w-x)*self.k + (h-y)*self.o
        if y == 1: SD = 0
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
        #print(len(minefield))
        for mine in minefield:
            if mine.x == self.x and mine.y == self.y:
                #print("Player Dead.")
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
        self.minefield = []
        self.is_mine = []
    def plant_mines(self):
        minefield = []
        for i in range(0, self.mines):
            minefield.append(len(minefield))
            while True:
                m = Mine(random.randint(1, self.width), random.randint(1, self.height))
                if [m.x, m.y] in self.is_mine:
                    pass
                else:
                    self.is_mine.append(len(self.is_mine))
                    self.is_mine[len(self.is_mine) - 1] = [m.x, m.y]
                    break
            minefield[len(minefield) - 1] = m
        self.minefield = minefield
        return minefield
def Game(f,p,n):
    rounds = 0
    while True:
        D = n.Decide(p.x,p.y,f.width,f.height) # 0:left,1:right,2:up,3:down

        if D == 0: # Move left
            p.move(-1,0)
            n.track.append(len(n.track))
            n.track[len(n.track) - 1] = [-1,0]
            new_mine = Mine(p.x + 1, p.y)

        elif D == 1: # Move Right
            p.move(1,0)
            n.track.append(len(n.track))
            n.track[len(n.track) - 1] = [1,0]
            new_mine = Mine(p.x - 1, p.y)

        elif D == 2: # Move Up
            p.move(0,1)
            n.track.append(len(n.track))
            n.track[len(n.track) - 1] = [0,1]
            new_mine = Mine(p.x, p.y - 1)
        elif D == 3: # Move Down
            p.move(0,-1)
            n.track.append(len(n.track))
            n.track[len(n.track) - 1] = [0,-1]
            new_mine = Mine(p.x, p.y + 1)
        else:
            print("[Error]: Invalid D: " + str(D))
            return 0

        f.minefield.append(len(f.minefield))
        f.minefield[len(f.minefield) - 1] = new_mine
        if p.is_alive(f.minefield) == False:
            break
        else:
            rounds += 1
    return rounds

#@jit(target ="cuda")
def Run():
    res = [0,None,None]
    amount_mines = 5
    f = Field(5,5,amount_mines)
    f.plant_mines()

    for mine in f.minefield:
        print("Mine:" + str(mine.x) + ':' + str(mine.y))
    wait = input("Enter... ")
    timestamp = time.time()
    simcount = 0
    while (time.time()-timestamp < 5):
        n = Neural_Network(tools.randomize(), tools.randomize(), tools.randomize(), tools.randomize(), tools.randomize(), tools.randomize(), tools.randomize(), tools.randomize(), tools.randomize(), tools.randomize(), tools.randomize(), tools.randomize(), tools.randomize(), tools.randomize(), tools.randomize(), tools.randomize())
        p = Player(1,1,f.width,f.height)
        r = Game(f,p,n)
        if r > res[0]:
            res = [r, n, f.minefield]
        f.minefield = f.minefield[:amount_mines]
        simcount += 1
    best = 0
    best_index = 0
    print(res)
    for mine in res[2]:
        print("Mine: " + str(mine.x) + ' : ' + str(mine.y))
    print("Track: " + str(res[1].track))
    print("Number of simulations: " + str(simcount))
    print(res[0])
#Run()
