def load_input(fname):
    with open(fname,'rt') as f:
        return f.read()

def evalWrittenSpace(idvalue,sindex,sz):
    #print('evaluating',idvalue,sindex,sz,sindex+sz-1)
    return int(idvalue*sz*(2*sindex+sz-1)/2)

def evaluate(bigstr):
    sz = len(bigstr)
    if sz%2 == 0:
        #the last one is spaces just remove it
        bigstr = bigstr[:-1]
    disk = [ int(x) for x in bigstr ]
    value = 0
    bss = 0#starting index of big string
    bse = sz-1 #end index of big string
    tidx = 0 #true index
    bsival = lambda idx : idx//2
    try:
        while True:
            #eval written part disk[bss]
            if bss%2==0:
                #print('evaluating data not about to move',disk[bss], bss,bse,)
                writtenSize = disk[bss]
                value += evalWrittenSpace(bsival(bss),tidx,writtenSize)
                tidx += writtenSize #move to another (free) block
                disk[bss] = 0
                bss += 1
            else:
                #print('moving right side to freespace',bss,bse)
                #fill+eval moved other part of disk
                freespace = disk[bss]
                tomovespace = disk[bse]
                #print(f'freespace {freespace}, tomove {tomovespace}')
                diff = freespace - tomovespace
                if diff>0:
                    disk[bss] -= tomovespace
                    disk[bse] -= tomovespace
                    value += evalWrittenSpace(bsival(bse),tidx,tomovespace)
                    tidx += tomovespace
                    disk[bse] = 0
                    bse -= 2
                elif diff<0:
                    disk[bse] -= freespace
                    disk[bss] -= freespace
                    value += evalWrittenSpace(bsival(bse),tidx,freespace)
                    tidx += freespace
                    disk[bss] = 0
                    bss += 1
                else:
                    #it's equal
                    value += evalWrittenSpace(bsival(bse),tidx,freespace)
                    tidx += freespace
                    disk[bse] = disk[bss] = 0
                    bse -= 2
                    bss += 1
                #print(disk)
                if bss>bse:
                    break
                pass
        pass
    except IndexError:
        #just stop evaluating
        pass
    return value
    
bigstr = load_input('input.txt')
#bigstr = load_input('input-test.txt')
#bigstr = "2333133121414131402"
#print(bigstr)
res = evaluate(bigstr)
print('solution1',res)

class DiskFile:
    def __init__(self,chvalue,space,pos = 0):
        self.value = chvalue
        self.space = space
        self.position = pos
    def __repr__(self):
        return f'(v {self.value}, s {self.space} at {self.position})'
    def moveTo(self,freemem):
        self.position = freemem.position
    def evaluate(self):
        return int(self.value*self.space*(2*self.position+self.space-1)/2)
    def isBefore(self,memchunk):
        return memchunk.position < self.position
    def canInsertIn(self,memchunk):
        return self.isBefore(memchunk) and self.space<=memchunk.space

class MemChunk:
    def __init__(self,space,position=0):
        self.space = space
        self.position = position
    def __repr__(self):
        return f'free mem of {self.space}, at {self.position}'
    def __lt__(self,val):
        return self.position<val.position
    def getPosition(self):
        return self.position
    def insertFile(self,file):
        if self.space>file.space:
            self.space -= file.space
            self.position += file.space
            return self
        elif self.space==file.space:
            self.space = 0
            self.position += file.space
            return MemChunk(0,1<<10)
        else:
            raise Exception('bad design!')

def getItemList(disk):
    sz = len(disk)
    #print(disk, sum(disk))
    files = []
    freesp = []
    pos = 0
    try:
        i = 0
        while i<sz:
            files.append( DiskFile(i//2,disk[i],pos) )
            pos += disk[i]
            i+=1
            freesp.append( MemChunk(disk[i],pos) )
            pos += disk[i]
            i+=1
    except:
        #print('exception, end of disk')
        pass
    #create also optimization helper
    freespdb = dict()
    for item in freesp:
        try:
            freespdb[item.space].append(item)
        except:
            freespdb[item.space] = [item]
    return files,freesp,freespdb

 #this optimization speed it up from 31s to 2.5s
def trytomovefile(opdb,file):
    cands = []
    #print(opdb)
    for i in range(file.space,10):
        try:
            lst = opdb[i]
            cands.append(lst[0])
        except:
            pass
    if len(cands)>0:
        cands.sort()
        freemem = cands[0]
        key = freemem.space        
        if file.canInsertIn(freemem):
            opdb[key].remove(freemem)
            file.moveTo(freemem)
            freemem.insertFile(file)
            opdb[freemem.space].append(freemem)
            opdb[freemem.space].sort()
    return

def evaluate2(bigstr):
    sz = len(bigstr)
    if sz%2 == 0:
        #the last one is spaces just remove it
        bigstr = bigstr[:-1]
    disk = [ int(x) for x in bigstr ]
    files,freesp,optdb = getItemList(disk)
    value = 0
    files.reverse()
    for file in files:
        #try to put it in free most-left chunk
        trytomovefile(optdb,file)
        """
        for freemem in freesp:
            #print(f'trying {freemem} for {file}')
            if file.canInsertIn(freemem):
                file.moveTo(freemem)
                freemem.insertFile(file)
        """
    return sum([x.evaluate() for x in files])

res = evaluate2(bigstr)
print('solution2',res)
