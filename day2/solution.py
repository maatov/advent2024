def load_input(fname):
    res = 0
    res2 = 0
    with open(fname,'rt') as f:
        for line in f:
            res += analyze([int(x) for x in line.split()])
            res2 += analyze2([int(x) for x in line.split()])
    return res, res2

def analyze(numlist):
    #safe: increase or decrease by 1-3
    return all([(numlist[i] - numlist[i+1]) in range(1,3+1) for i in range(len(numlist)-1)]) or all([(numlist[i+1] - numlist[i]) in range(1,3+1) for i in range(len(numlist)-1)])

def analyze2(nlist):
    res = analyze(nlist)
    if not res:
        #search for dumpener blindly
        for i in range(len(nlist)):
            nlistcopy = nlist[:]
            nlistcopy = nlist[:i] + nlist[i+1:]
            #print(nlist,nlistcopy)
            if analyze(nlistcopy):
                return True
        return False
    else:
        return True
    

sol1,sol2 = load_input('test-input.txt')
sol1,sol2 = load_input('input.txt')
print(f"solution1 {sol1}, solution2 {sol2}")