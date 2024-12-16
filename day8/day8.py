from itertools import combinations

def load_input(fname):
    with open(fname,'rt') as f:
        return [ x.strip() for x in f.readlines()]

def analyze_input(mtx):
    antenaes = dict()
    for i in range(len(mtx)):
        for j in range(len(mtx[0])):
            if mtx[i][j]!='.':
                try:
                    antenaes[mtx[i][j]] += [(i,j)]
                except:
                    antenaes[mtx[i][j]] = [(i,j)]
    #print(antenaes)
    return antenaes

def getantinodes(p1,p2):
    x,y = p1
    x2,y2 = p2
    anx,any = 2*x-x2,2*y-y2
    anx2,any2 = 2*x2-x,2*y2-y
    return [(anx,any),(anx2,any2)]
    

def count_antinodes(listofantenaes,maxx,maxy):
    anset = set()
    for ant in listofantenaes:
        for pair in combinations(listofantenaes[ant],2):
            for an in getantinodes(pair[0],pair[1]):
                x,y = an
                if x in range(0,maxx) and y in range(0,maxy):
                    anset.add((x,y))
    return len(anset)

#mtx = load_input('input-test.txt')
mtx = load_input('input.txt')
res = count_antinodes(analyze_input(mtx),len(mtx),len(mtx[0]))
print('solution1',res)

#with resonance harmonics
def getantinodesrh(p1,p2,bx,by):
    x,y = p1
    x2,y2 = p2
    dx,dy = x-x2,y-y2
    dx2,dy2 = x2-x,y2-y
    irange = range(-bx.stop,bx.stop)
    return [(x+i*dx,y+i*dy) for i in irange if x+i*dx in bx and y+i*dy in by]

def count_antinodes_rh(listofantenaes,bx,by):
    anset = set()
    for ant in listofantenaes:
        for pair in combinations(listofantenaes[ant],2):
            for an in getantinodesrh(pair[0],pair[1],bx,by):
                x,y = an
                anset.add((x,y))
    return len(anset)

res = count_antinodes_rh(analyze_input(mtx),range(0,len(mtx)),range(0,len(mtx[0])))
print('solution2',res)