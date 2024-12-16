
def loadinput(fname):
    with open(fname,'rt') as f:
        return [x.strip() for x in f.readlines()]

class PlantRegion:
    def __init__(self,plant):
        self.plant = plant
        self.area = 0
        self.perimeter = 0
    def update(self,area,perimeter):
        self.area += area
        self.perimeter += perimeter
    def __repr__(self):
        return f"({self.plant},{self.area},{self.perimeter})"
    def evaluate(self):
        return self.area * self.perimeter
    
N,E,S,W = 0,1,2,3
TONESW = [(-1,0),(0,1),(1,0),(0,-1)]
def tryregion(ptype,x,y,garden,walklog,borderlog):
    try:
        if x<0 or y<0:
            return (0,1)
        if (x,y) in walklog:
            return (0,0)
        if garden[x][y]!=ptype:
            return (0,1)
        else:
            walklog.add((x,y))
            a,p = 1,0
            for dx,dy in TONESW:
                (da,dp) = tryregion(ptype, x+dx, y+dy, garden,walklog,borderlog)                
                a += da
                p += dp
                if dp in range(1,5):
                    borderlog.add((x,y))
                pass
        #print(f'coords ({x},{y}) and vals {da}, {dp}')
        return (a,p)
    except IndexError:
        return (0,1)
    return (0,0)

def getPlantInfoFromNextRegion(inp,wr):
    for x in range(len(inp)):
        for y in range(len(inp[x])):
            if (x,y) not in wr:
                return (inp[x][y],x,y)
    raise Exception("end")


def getFenceBulks(borderpoints):
    print(borderpoints)
    rows = dict([(x,[]) for (x,y) in borderpoints])
    cols = dict([(y,[]) for (x,y) in borderpoints])
    for (x,y) in borderpoints:
        rows[x].append(y)
        cols[y].append(x)
    print('by rows',rows)
    print('by cols', cols)
    
    
inp = loadinput('input-test.txt')
#inp = loadinput('input.txt')
inp = [ [x for x in line] for line in inp]
#solution 1
sol = []
try:
    walkedregions = set()
    while True:
        p,x,y = getPlantInfoFromNextRegion(inp,walkedregions)
        temp = set()
        borderplants = set()
        a,p = tryregion(p,x,y,inp,temp,borderplants)
        sol.append((a,p,(p,x,y)))
        walkedregions = walkedregions.union(temp)
except:
    pass

def enlarge(mtx):
    #put one line and one col between any 2 points
    newm = []
    newm.append(['-' for x in range(len(mtx[0])*2+1)])
    for line in mtx:
        tmp = ['|']        
        for x in line:
            tmp.append(x)
            tmp.append('?')
        tmp[-1] = '|'
        newm.append(tmp)
        newm.append(['-' for x in range(len(line)*2+1)])
    for x in range(1,len(newm)-1,2):
        for y in range(1,len(newm[x])-1):
            if newm[x][y]=='?':
                #look around
                try:
                    if newm[x][y-1]==newm[x][y+1]:
                        newm[x][y] = newm[x][y-1]
                    else:
                        newm[x][y] = '|'
                except:
                    newm[x][y] = '|'
    for x in range(2,len(newm)-1,2):
        for y in range(len(newm[x])):
            try:
                u = newm[x-1][y]
                if u==newm[x+1][y]:
                    newm[x][y] = u
                else:
                    newm[x][y] = '-'
                
            except:
                pass
    for x in range(0,len(newm),2):
        for y in range(0,len(newm[x]),2):
            try:
                TOWE = [(0,-1),(0,1)]
                TONS = [(-1,0),(1,0)]
                if newm[x][y] in {'-'} and any([newm[x+dx][y+dy] in {'|'} for dx,dy in TONS]):
                    newm[x][y] = '+'
                if newm[x][y] in {'|'} and any([newm[x+dx][y+dy] in {'-'} for dx,dy in TOWE]):
                    newm[x][y] = '+'
            except:
                pass
                
                    
    #point (x,y) will map to (1+x*2,1+y*2)
    return newm

for item in sol:
    print(item)
print('solution1',sum([a*b for a,b,x in sol]))

#solution 2
inp2 = enlarge(inp)
print(inp2)
for line in inp2:
    print(''.join(line))