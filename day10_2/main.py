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
        xbase = ax
        ybase = ay
        ibase = i
print(cmax)

# part 2
# 1) eliminisati sve asteroide koji nisu u sightu jer je njih 267 > 200 
# u sightu, pa ce vec u prvom krugu biti unisteno svih 200 
# 2) naci i eliminisati prvih 200 koji su u sightu

for i in range(0, len(data)):
   if i != ibase and sight(xbase,ybase,i%w,int(i/w)) == False:
       data = data[:i] + '.' + data[i+1:]

#iscrtati samo one koje su u sightu
def plot():
    for i in range(0, len(data)):
        c = data[i]
        if i == ibase:
            c = '█' 
        if (i + 1)%w != 0:
            print(c, end = "")
        else:
            print(c)


def findNext():
    besti = 0
    bestCriterium = 0
    mode = 0    #inicijalno 0, leva poluravan -1, desna poluravan 1
    ind = 0

    for i in range(0, len(data)):
        if i != ibase and data[i] == '#':
            bx = i%w
            by = int(i/w)
            x = bx - xbase #relative x
            y = by - ybase #relative y
            if x == 0 and y < 0:
                return i
            elif mode == 0:
                 besti = i
                 mode = -1
            elif x > 0 and mode == -1:
                mode = 1
                besti = i
                bestCriterium = y/x
            elif x == 0 and y > 0 and mode == -1:
                mode = 1
                besti = i
                bestCriterium = float('Inf')
            elif x < 0 and y > 0 and mode == -1 and -y/x > bestCriterium:
                ind = 1
                besti = i
                bestCriterium = -y/x
            # elif x < 0 and y == 0 and mode == -1 and ind == 0:
            #     besti = i
            #     bestCriterium = 0
            elif x < 0 and y <= 0 and mode == -1 and ind == 0 and (y/x <= bestCriterium or bestCriterium == 0):
                besti = i
                bestCriterium = y/x
            elif x > 0 and mode == 1 and y/x < bestCriterium:
                besti = i
                bestCriterium = y/x
    return besti


for i in range(0,200):  #200. asteroid je za i = 198
    index = findNext()
    data = data[:index] + '.' + data[index + 1:]
    print(i)
    print("xrel = " + str(index%w - xbase))
    print("yrel = " + str(int(index/w - ybase)))
    print("xaps = " + str(index%w))
    print("yaps = " + str(int(index/w)))
print("xbase = " + str(xbase))
print("ybase = " + str(ybase))

plot()
            
            