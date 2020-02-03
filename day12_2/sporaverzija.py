import numpy as np

class Moon:
    x = 0
    y = 0
    z = 0
    xv = 0
    yv = 0
    zv = 0
    def __init__(self, x,y,z, xv = 0, yv = 0, zv = 0):
        self.x = x
        self.y = y
        self.z = z
        self.xv = xv
        self.yv = yv
        self.zv = zv
    
    def energy(self):
        return (abs(self.x) + abs(self.y) + abs(self.z)) * (abs(self.xv) + abs(self.yv) + abs(self.zv)) 

    def ispis(self):
        print("(x,y,z) = (" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")\n(xv,yv,zv) = (" + str(self.xv) + "," + str(self.yv) + "," + str(self.zv) + ")")

def different(p, q):
    for i in range(0,len(p)):
        a = p[i]
        b = q[i]
        if a.x != b.x or a.y != b.y or a.z != b.z or a.xv != b.xv or a.yv != b.yv or a.zv != b.zv:
            return True
    return False

origstate = []
moons = []
newmoons = []

f = open("C:\D\Visual Studio Code\day12\input.txt")
data = f.readlines()

for i in data:
    x = int(i.rsplit('=')[1].rsplit(',')[0])
    y = int(i.rsplit('=')[2].rsplit(',')[0])
    z = int(i.rsplit('=')[3].rsplit('>')[0])
    moons.append(Moon(x,y,z))
    newmoons.append(Moon(x,y,z))
    origstate.append(Moon(x,y,z))

s = 0

while different(moons,origstate) or s == 0:
    s += 1
    print(s)
    for i in range(0,len(moons)):
        for j in range(i+1,len(moons)):
            xs = np.sign(moons[i].x - moons[j].x)
            ys = np.sign(moons[i].y - moons[j].y)
            zs = np.sign(moons[i].z - moons[j].z)
            newmoons[i].xv -= xs
            newmoons[j].xv += xs
            newmoons[i].yv -= ys
            newmoons[j].yv += ys
            newmoons[i].zv -= zs
            newmoons[j].zv += zs

    for i in range(0,len(moons)):
        newmoons[i].x += newmoons[i].xv
        newmoons[i].y += newmoons[i].yv
        newmoons[i].z += newmoons[i].zv

    moons = newmoons

print(s)
