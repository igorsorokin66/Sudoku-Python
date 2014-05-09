class Square:
    def __init__(self):
        self._possi = [x for x in range(1,10)]
    def setData(self, val):
        self._val = val
    def getData(self):
        return self._val
    def setPossi(self,possi):
        self._possi = possi
    def getPossi(self):
        return self._possi
    def remove(self,remove):
        self._possi = set(self._possi) - set([remove])

grid = [[Square() for x in range(10)] for x in range(10)]

line = []
b = 1
box = {}
for Y in range(1,10,3):
    for X in range(1,10,3):
        for x in range(Y,Y+3):
            for y in range(X,X+3):
                line.append([x,y])
        box[b] = line
        line = []
        b+=1

def whichBox(x,y):
    res = 1
    if y > 6:
        res += 2
    elif y > 3:
        res += 1
    if x > 6:
        res += 6
    elif x > 3:
        res += 3
    return res

def removePossi(l,i,val):
    for x in range(1,10):
        grid[l][x].remove(val)
    for y in range(1,10):
        grid[y][i].remove(val)
    for o in box[whichBox(l,i)]:
        grid[o[0]][o[1]].remove(val)

def init():
    for l in range(1,len(raw)):
        for i in range(0,9):
            if raw[l][i] != "0" and raw[l][i] != ' ':
                grid[l][i+1].setData(int(raw[l][i]))
                removePossi(l,i+1,int(raw[l][i]))
            else:
                grid[l][i+1].setData(' ')

def possi(x,y):
    possi = [x for x in range(1,10)]
    for ny in range(1,10):
        possi = set(possi) - set([grid[x][ny].getData()])
    for nx in range(1,10):
        possi = set(possi) - set([grid[nx][y].getData()])
    for o in box[whichBox(x,y)]:
        possi = set(possi) - set([grid[o[0]][o[1]].getData()])#: {8, 9, 2, 4, 5}
    if len(grid[x][y].getPossi()) < len(list(possi)):
        dd = 1
    else:
        grid[x][y].setPossi(list(possi))
    return list(grid[x][y].getPossi())
    #return list(set(possi)&set(grid[x][ny]._possi))#SOMETHING AROUND HERE

def findHori(x,y,possiC):
    for h in range(1,10):
        if grid[x][h].getData() == ' ' and h != y:
            possiC = set(possiC) - set(possi(x,h))
    return list(possiC)
        
def findVert(x,y,possiC):
    for v in range(1,10):
        if grid[v][y].getData() == ' ' and v != x:
            possiC = set(possiC) - set(possi(v,y))
    return list(possiC)

def findBox(x,y,possiC):
    for o in box[whichBox(x,y)]:
        if grid[o[0]][o[1]].getData() == ' ' and not(o[0] == x and o[1] == y):
            possiC = set(possiC) - set(possi(o[0],o[1]))
    return list(possiC)

def solve(x,y):
    possiC = possi(x,y)
    if len(possiC) == 1:
        grid[x][y].setData(possiC[0])
        removePossi(x,y,possiC[0])
        printGrid()
        return True
    else:
        possiS = [findHori(x,y,possiC),findVert(x,y,possiC), findBox(x,y,possiC)]
        for p in possiS:
            if len(p) == 1:
                grid[x][y].setData(p[0])
                removePossi(x,y,p[0])
                printGrid()
                return True
            
def solve1(x,y):
    rets = False
    possiC = possi(x,y)
    for n in possiC:#for naked two's like 13 and 13
        found = []
        for o in box[whichBox(x,y)]:
            if n in possi(o[0],o[1]) and grid[o[0]][o[1]].getData() == ' ' and not(o[0] == x and o[1] == y):
                found.append(o)
        if len(found) == 1:
            if x == found[0][0]:
                for h in range(1,10):
                    if grid[x][h].getData() == ' ' and h != y and h != found[0][1]:
                        grid[x][h].remove(n)
                        rets = True
            if y == found[0][1]:
                for v in range(1,10):
                    if grid[v][y].getData() == ' ' and v != x and v != found[0][0]:
                        grid[v][y].remove(n)
                        rets = True
            for u in box[whichBox(x,y)]:
                if grid[u[0]][u[1]].getData() == ' ' and u != [x,y] and u != found[0]:
                        grid[u[0]][u[1]].remove(n)
                        rets = True
    nums = {}            
    for o in box[whichBox(x,y)]:
        if grid[o[0]][o[1]].getData() == ' ':
            possiO = grid[o[0]][o[1]].getPossi()
            for p in possiO:
                if p in nums.keys():
                    nums[p].append(o)
                else:
                    nums[p] = [o]
    found = []#2, 
    for n in nums.keys():
        if len(nums[n]) == 2:
            found.append([n,nums[n]])
    sqrs = {}
    for f in found:
        jk = str(f[1][0][0])+str(f[1][0][1])+str(f[1][1][0])+str(f[1][1][1])
        if jk in sqrs.keys():
            sqrs[jk].append(f[0])
        else:
            sqrs[jk] = [f[0]]
    for s in sqrs.keys():
        if len(sqrs[s]) == 2:
            if s[0] == s[2]:
                for h in range(1,10):
                    if grid[int(s[0])][h].getData() == ' ' and h != int(s[1]) and h != int(s[3]):
                        grid[int(s[0])][h].remove(sqrs[s][0])
                        grid[int(s[0])][h].remove(sqrs[s][1])
                        rets = True
                    elif h == int(s[1]) or h == int(s[3]):
                        grid[int(s[0])][h].setPossi(sqrs[s])
            if s[1] == s[3]:
                for v in range(1,10):
                    if grid[v][int(s[1])].getData() == ' ' and v != int(s[0]) and v != int(s[2]):
                        grid[v][int(s[1])].remove(sqrs[s][0])
                        grid[v][int(s[1])].remove(sqrs[s][1])
                        rets = True
                    elif v == int(s[0]) or v == int(s[2]):
                        grid[v][int(s[1])].setPossi(sqrs[s])
    
    found = []  #2,6,3
    sqr2num = {}#abc - 2,6
    for n in nums.keys():
        if len(nums[n]) == 3:
            found.append(n)
            key = str(nums[n][0])+str(nums[n][1])+str(nums[n][2])
            if key in sqr2num.keys():
                sqr2num[key].append(n)
            else:
                sqr2num[key] = [n]
    for sn in sqr2num.keys():
        if len(sqr2num[sn]) != 2:
            found.remove(sqr2num[sn][0])#2,6
    if len(found) != 2:
        return rets
    for n in nums.keys():#[[5, 5], [5, 6], [6, 6]] 
        if len(nums[n]) == 2 and set([str(nums[n][0][0])+str(nums[n][0][1]), str(nums[n][1][0])+str(nums[n][1][1])]).issubset(set([str(nums[found[0]][0][0])+str(nums[found[0]][0][1]),str(nums[found[0]][1][0])+str(nums[found[0]][1][1]),str(nums[found[0]][2][0])+str(nums[found[0]][2][1])])):#ab in abc
            found.append(n)
    if len(found) != 3:
        return rets
    for f in found:
        for n in nums[f]:
            grid[n[0]][n[1]].setPossi(list(set(grid[n[0]][n[1]].getPossi())&set(found)))
            rets = True
    return rets      

def printGrid():
    print("-------------")
    for x in range(1,10):
        print("|",end='')
        for y in range(1,10):
            if y == 3 or y == 6 or y == 9:
                print(str(grid[x][y].getData())+"|",end='')
            else:
                print(grid[x][y].getData(),end='')
        if x == 3 or x == 6 or x == 9: 
            print()
            print("-------------")
        else:
            print()

raw = []
raw.append("")
file = open('input20.txt')
lines = file.readlines()

z = 0
k = 9
for r in range(0,1):
    raw = []
    raw.append("")
    #print(lines[z-1])
    for l in range(z,k):
        raw.append(lines[l])
    init()
    printGrid()
    flag = False
    while True:
        for x in range(1,10):
            for y in range(1,10):
                if grid[x][y].getData() == ' ':
                    if solve(x,y):
                        flag = False
        if flag:
            for x in range(1,10):
                for y in range(1,10):
                    if grid[x][y].getData() == ' ':
                        if solve1(x,y):
                            flag = False
        if flag:
            break
        flag = True
    z+=10
    k+=10
    printGrid()
    grid = [[Square() for x in range(10)] for x in range(10)]