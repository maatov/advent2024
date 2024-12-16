import re

def load_input(fname):
    with open(fname) as f:
        tmap = f.readlines()
        tmap = [x.strip() for x in tmap]
        return tmap

def getStartingPoints(tmap:str):
    x = 0
    points = set()
    for line in tmap:
        indices = [match.start() for match in re.finditer("0", line)]
        for i in indices: points.add((x,i))
        x += 1
    return points

N=0
E=1
S=2
W=3
vdiff = [(-1,0), (0,1), (1,0), (0,-1)]
ndir = lambda d,x,y: (x+vdiff[d][0],y+vdiff[d][1])
def findTrail(tmap,spoint,value,removeFinal):
    #sum of all directions
    try:
        x,y = spoint
        if x<0 or y<0:
            return 0
        if tmap[x][y]!=value:
            return 0
        if tmap[x][y]==9:
            #found trail
            if removeFinal: #remove if we are interested in finding just one trail start to peak
                tmap[x][y] = -1
            return 1
        return sum([findTrail(tmap,ndir(d,x,y),value+1,removeFinal) for d in [N,E,S,W]])
    except IndexError:
        return 0

def findTrailFromOnePoint(tmap,spoint):
    mapcopy = [l[:] for l in tmap] #deepcopy
    return findTrail(mapcopy,spoint,0,True)

#tmap = load_input('input-test.txt')
tmap = load_input('input.txt')
spoints = getStartingPoints(tmap) #starting points
tmapi = [[int(x) for x in line] for line in tmap]
sol1 = sum([findTrailFromOnePoint(tmapi,(x,y)) for (x,y) in spoints])
print('solution 1',sol1)
sol2 = sum([findTrail(tmapi,(x,y),0,False) for (x,y) in spoints])
print('solution 2', sol2)
