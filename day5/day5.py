def load_input(fname):
    with open(fname,'rt') as f:
        loadingPageOrder = False
        precrules = []
        updates = []
        prsetnegative = set() #set of page order violations
        for line in f:
            line = line.strip()
            if len(line)==0:
                loadingPageOrder = True
                continue
            if loadingPageOrder:
                updates.append(line.split(','))
            else:
                a,b = line.split('|')
                prsetnegative.add(b+"!"+a)
                pass
    return prsetnegative,updates

def evaluate(pagelist,vruleset):
    #if updatelist it is valid it returns middle page number
    for i in range(len(pagelist)-1):
        for j in range(i+1,len(pagelist)):
            #check violation
            key = pagelist[i]+"!"+pagelist[j]
            if key in vruleset:
                #violation!
                return 0
    #no violations then it is good
    return int(pagelist[len(pagelist)//2])

def solution1(updatelist,nrules):
    res = 0
    for update in updatelist:
        res += evaluate(update,nrules)
    return res

def solution2(updatelist,nrules):
    return sum([eval2(x,nrules) for x in updatelist])

def eval2(plist,vrules):
    corrected = False
    originallyCorrect = True
    while not corrected:
        for i in range(len(plist)-1):
            for j in range(i+1,len(plist)):
                #check violation
                a,b = plist[i], plist[j]
                key = a+"!"+b
                if key in vrules:
                    #violation! -> let's correct it by swap
                    originallyCorrect = False
                    plist[i] = b
                    plist[j] = a
                    continue
                pass
            pass
        corrected = True
    return 0 if originallyCorrect else int(plist[len(plist)//2])

vs,u = load_input('input-test.txt')
vs,u = load_input('input.txt')
print('solution1',solution1(u,vs))
print('solution1',solution2(u,vs))
