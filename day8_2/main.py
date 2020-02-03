
def draw(x,y,p,c0,c1,c2):
    for i in range(0,y):
        for j in range(0,x):
            if(p[i*x+j] == "0"):
                print(c0, end = "")
            elif(p[i*x+j] == "1"):
                print(c1, end = "")
            else:
                print(c2, end = "")
        print()
f = open("C:\D\Visual Studio Code\day8\input.txt")
data = f.read()
x = 25
y = 6
pix = x*y
out = []
j = 0

for i in range(0,pix):
    while data[j*pix+i] == "2":
        j += 1
    out.append(data[j*pix+i])
    j = 0

draw(x,y,out," ","█","")

#█