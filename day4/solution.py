
def load_input(fname):
    with open(fname,'rt') as f:
        data = f.read()
    matrixl = []
    for line in data.split():
        matrixl.append([Node(x) for x in list(line.strip())])
    return matrixl

class Node:
    def __init__(self,val):
        self.sval = val
        self.content = False
    def __repr__(self):
        return "." if self.content else "?" + str(self.sval)
    def value(self):
        return self.sval
    def flagit(self):
        self.content = True

def findXMAS(matrix):
    directionmodif = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    vsize = len(matrix)
    hsize = len(matrix[0])
    sol = 0
    for l in range(vsize):
        for c in range(hsize):
            for dir in directionmodif:
                dx,dy = dir
                sol += lookupindirection(matrix,l,c,dx,dy)
    return sol

def lookupindirection(matrix,x,y,dx,dy):
    WORD = "XMAS"
    ox,oy = x,y
    for w in WORD:
        try:
            if x>=0 and y>=0 and w==matrix[x][y].value():
                x += dx
                y += dy
            else:
                return 0
        except IndexError as e:
            return 0
    return 1

def findX_MAS(matrix):
    sol = 0
    sizev,sizeh = len(matrix), len(matrix[0])
    for l in range(1,sizev-1):
        for c in range(1,sizeh-1):
            if matrix[l][c].value()=='A':
                sol += isourX(matrix,l,c)
    return sol

def isourX(mtx,x,y):
    VALIDRES = {"MS","SM"}
    dirsw1 = [ (-1,-1),(1,1) ]
    dirsw2 = [ (1,-1),(-1,1) ]
    w1 = ''.join([ mtx[x+dx][y+dy].value() for dx,dy in dirsw1 ])
    w2 = ''.join([ mtx[x+dx][y+dy].value() for dx,dy in dirsw2 ])    
    return 1 if w1 in VALIDRES and w2 in VALIDRES else 0

matrixl = load_input('input-test.txt')
matrixl = load_input('input.txt')
print('solution1',findXMAS(matrixl))
print('solution2',findX_MAS(matrixl))
