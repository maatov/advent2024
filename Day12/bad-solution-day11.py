
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

def updateplantstat(plantstat,plant,area,perimeter):
    try:
        plantstat[plant].update(area,perimeter)
    except KeyError:
        pl = PlantRegion(plant)
        pl.update(area,perimeter)
        plantstat[plant] = pl

def analyzeGardenByLines(imtx,plants):
    for line in imtx:
        ptype = 'unused'
        a = 0
        p = 0
        for pl in line:
            if pl!=ptype:
                updateplantstat(plants,ptype,a,p+1)
                ptype = pl
                a,p = 1,1
            else:
                a += 1
        updateplantstat(plants,ptype,a,p+1)
    del plants["unused"]
    return plants

def getInvertedGarden(imtx):
    m,n = len(imtx),len(imtx[0])
    return [ [imtx[i][j] for i in range(m)] for j in range(n) ]

inp = loadinput('input-test.txt')
print(inp)
plants = dict()
plants = analyzeGardenByLines(inp,plants)
plants = analyzeGardenByLines(getInvertedGarden(inp),plants)
#div by 2
for plant in plants:
    p = plants[plant]
    p.area //= 2
    print(p)
sol1 = sum([plants[x].evaluate() for x in plants])
print('solution1',sol1)