
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
            if p>0:
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
        res = tryregion(p,x,y,inp,temp,borderplants)
        #print(f'region walkedthrough {p},({x},{y}), result: {res}')
        print(f'border plants {borderplants}')
        sol.append(res)
        walkedregions = walkedregions.union(temp)
        borderbulks = getFenceBulks(borderplants)
        break
except:
    pass

    
print('solution1',sum([a*b for a,b in sol]))

#solution 2