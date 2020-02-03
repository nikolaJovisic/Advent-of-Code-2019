import math

f = open("C:\D\Visual Studio Code\day10\input.txt")
data = f.read()

w = 0
while data[w] != "\n":
    w += 1

data = data.replace("\n","")

cmax = 0

def sight(ax,ay,bx,by):
    xstep = ax - bx
    ystep = ay - by
    gcd = math.gcd(xstep,ystep)
    if gcd == 1:
        return True
    xstep /= gcd
    ystep /= gcd
    by += ystep
    bx += xstep
    while bx != ax or by != ay:
        if data[int(w*by+bx)] == '#':
            return False   
        bx += xstep
        by += ystep
    return True



for i in range(0,len(data)):
    if data[i] != '#':
        continue
    ax = i%w
    ay = int(i/w)
    ac = 0
    for j in range(0,len(data)):
        if data[j] != '#' or i == j:
            continue
        bx = j%w
        by = int(j/w)
        if sight(ax,ay,bx,by):
            ac += 1
    if ac > cmax:
        cmax = ac

print(cmax)