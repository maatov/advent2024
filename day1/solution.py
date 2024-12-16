import time

def load_input(fname):
    with open(fname,'rt') as f:
        col1,col2 = [],[]
        stats = {}
        for l in f:
            a,b = tuple([int(x) for x in l.split()])
            col1.append(a)
            col2.append(b)
            try:
                stats[b] += 1
            except:
                stats[b] = 1
        return col1,col2,stats

def ccol(nums,stats):
    rv = []
    for i in nums:
        try:
            rv.append((i,stats[i]))
        except:
            rv.append((i,0))
    return rv

#c1,c2,s = load_input('input.test.txt')
c1,c2,s = load_input('input.txt')
c1.sort()
c2.sort()
print('solution1',sum([abs(x-y) for x,y in zip(c1,c2)]))
print('solution2',sum([a*b for a,b in ccol(c1,s)]))
