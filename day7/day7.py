def load_input(fname):
    with open(fname,'rt') as f:
        input = []
        for line in f:
            s1 = line.split(':')
            s2 = s1[1].split()
            input.append((int(s1[0]),[int(x) for x in s2]))
    return input

def tryoperatorcomb(result,numbers,opset):
    #print('evaluating',result,numbers,len(opset))
    init = numbers[0]
    i = 1
    for op in opset:
        init = op(init,numbers[i])
        i+=1
    return result == init

plus = lambda a,b:a+b
mult = lambda a,b:a*b
conc = lambda a,b:int(str(a)+str(b))
def getopset(size,itempart):
    ip = itempart + [plus]
    im = itempart + [mult]
    if size==1:
        return [ip] + [im]
    else:
        return getopset(size-1,ip) + getopset(size-1,im)

def evaluate(data):
    result,nums = data
    #possible operators +,* eval from left to right w/o priority
    return result if any([tryoperatorcomb(result,nums,x) for x in getopset(len(nums)-1,[])]) else 0

def solution1(input):
    return sum([evaluate(x) for x in input])

#pato pouzil nejaky itertools.product co taketo vyraba
def getopset2(size,itempart):
    ip = itempart + [plus]
    im = itempart + [mult]
    ic = itempart + [conc]
    if size==1:
        return [ip] + [im] + [ic]
    else:
        return getopset2(size-1,ip) + getopset2(size-1,im) + getopset2(size-1,ic)

def evaluate2(data):
    result,nums = data
    #possible operators +,* eval from left to right w/o priority
    return result if any([tryoperatorcomb(result,nums,x) for x in getopset2(len(nums)-1,[])]) else 0

def solution2(input):
    return sum([evaluate2(x) for x in input])

#input = load_input('input-test.txt')
input = load_input('input.txt')
print('solution1',solution1(input))
print('solution2',solution2(input))

