def load_input(fname):
    with open(fname,'rt') as f:
        mp = [ list(l.strip()) for l in f.readlines() ]
        rv = []
        rowi = 0
        for line in mp:
            rcoli = iter(range(len(line)))
            rv.append([Node(x,rowi,next(rcoli)) for x in line])
            try:
                scol = line.index('^')
                srow = rowi
                rv[rowi][scol].covered = True
            except ValueError:
                pass
            rowi += 1
        return (rv,(srow,scol))

N = 0
E = 1
S = 2
W = 3

class Node:
    def __init__(self,val,x,y):
        self.obstacle = val=='#'
        self.covered = False
        self.impactside = set()
        self.artificialObstacle = False
        self.coord = (x,y)
    def __repr__(self):
        return '#' if self.obstacle else '.' if not self.covered else 'O' if self.artificialObstacle else 'x'
    def __eq__(self,val):
        return val==self.__repr__()
    def isfree(self):
        return not self.obstacle
    def isobstacle(self):
        return self.obstacle
    def occupy(self):
        self.covered = True
    def guardFacedObstacleTo(self,isd):
        self.impactside.add(isd)
    def putArtificialObstacle(self):
        self.obstacle = True
    def removeArtificialObstacle(self):
        self.obstacle = False
    def coords(self):
        return self.coord
    def isFacedObstacle(self):
        return self.obstacle and len(self.impactside)>0
    
def paint_map(mp,sx,sy):
    #facing north at the sx,sy
    ax,ay = sx,sy
    #NESW
    ad = N
    nextDir = [ (-1,0), (0,1), (1,0), (0,-1) ]
    turnDir = [ E, S, W, N ]
    nextstep = lambda d,x,y: (x+nextDir[d][0],y+nextDir[d][1])
    while True:
        try:
            #print('at position',ad,ax,ay)
            if ax<0 or ay<0:
                break
            #occupy position
            mp[ax][ay].occupy()
            nx,ny = nextstep(ad,ax,ay)
            #next step
            if mp[nx][ny].isfree():
                ax,ay = nx,ny
            else:
                mp[nx][ny].guardFacedObstacleTo(ad)
                ad = turnDir[ad]
            pass
        except:
            break
        pass
    pass

def count_occupied(mp):
    return sum([x.count('x') for x in mp])

def getAllFacedObstacles(mp):
    return [ l for mpline in mp for l in mpline if l.isFacedObstacle()]

def canReachLoop(mp,d,x,y):
    MAXX = len(mp)
    MAXY = len(mp[0])
    NEXTDIR = [ (-1,0), (0,1), (1,0), (0,-1) ]
    TURNRIGHT = [ E, S, W, N ]
    nextStep = lambda d,x,y: (x+NEXTDIR[d][0],y+NEXTDIR[d][1])
    visitedObstacles = set()
    ax,ay = x,y
    try:
        while True:
            #lookup
            nx,ny = nextStep(d,ax,ay)
            if nx<0 or ny<0:
                return False
            if mp[nx][ny].isobstacle():
                if (d,nx,ny) in visitedObstacles:
                    #bingo! we are in loop
                    return True
                else:
                    #just turn and continue
                    visitedObstacles.add((d,nx,ny))
                    d = TURNRIGHT[d]
            else:
                ax,ay = nx,ny
    except IndexError:
        return False
    pass

def analyzeLibrary(mp,sx,sy):
    #facing north at the sx,sy
    ax,ay = sx,sy
    #NESW
    ad = N
    nextDir = [ (-1,0), (0,1), (1,0), (0,-1) ]
    turnDir = [ E, S, W, N ]
    nextstep = lambda d,x,y: (x+nextDir[d][0],y+nextDir[d][1])
    artificalObstacles = set()
    visitedNodes = set()
    try:
        #have to start one step further
        #ax,ay = nextstep(ad,ax,ay)
        while True:
            #print('at position',ad,ax,ay)
            visitedNodes.add((ax,ay))
            nx,ny = nextstep(ad,ax,ay)
            if nx<0 or ny<0:
                break
            if mp[nx][ny].isfree():
                #put artificial obstacle if is not in already walked path
                if (nx,ny) not in visitedNodes:
                    #print('trying',(nx,ny))
                    mp[nx][ny].putArtificialObstacle()                    
                    if canReachLoop(mp,ad,ax,ay):
                        #print('found one!',nd,nx,ny)
                        artificalObstacles.add((nx,ny))
                    mp[nx][ny].removeArtificialObstacle()
                #move on
                ax,ay = nx,ny
            else:
                #obstacle: let's turn and continue
                ad = turnDir[ad]
        pass
    except:
        pass
    print('number of visited nodes:',len(visitedNodes))
    return len(artificalObstacles)

#mp,(sx,sy) = load_input('input-test.txt')
mp,(sx,sy) = load_input('input.txt')
paint_map(mp,sx,sy)
print('solution1',count_occupied(mp))

#solution2
#print(mp,sx,sy)
res = analyzeLibrary(mp,sx,sy)
print('solution2',res)
