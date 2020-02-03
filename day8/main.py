f = open("C:\D\Visual Studio Code\day8\input.txt")
data = f.read()

ind = 0
sgl = float('Inf')

for i in range(0,100):
    s = 0
    for j in range(0,150):
        if data[i*100+j] == "0":
            s += 1
    if s < sgl:
        sgl = s
        ind = i

j = 0
d = 0

for i in range(0,150):
    if data[ind*100+i] == "1":
        j += 1
    if data[ind*100+i] == "2":
        d += 1

print(j*d)






