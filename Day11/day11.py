
def blinkstone(x):
    sx = str(x)
    if x==0:
        return [1]
    elif len(sx)%2==0:
        sppoint = len(sx)//2
        return [int(sx[:sppoint]), int(sx[sppoint:])]
    else:
        return [x*2024]
    
def blinkvec(vec,iters):
    vecd = dict([(x,1) for x in vec])
    #print(vecd)
    for i in range(iters):
        tmp = dict()
        for k in vecd:
            count = vecd[k]
            afterb = blinkstone(k)
            for item in afterb:
                try:
                    tmp[item] += count
                except:
                    tmp[item] = count
        #print(i,tmp)
        vecd = tmp
        #print(f' after {i} iter, partial sum is {sum([vecd[x] for x in vecd])}')
    count = sum([vecd[x] for x in vecd])
    #print(vecd)
    #print(count,len(vecd))
    return count

inputtext = "125 17"
inputtext = "965842 9159 3372473 311 0 6 86213 48"
#inputtext = "0"
stonelist = [int(x) for x in inputtext.split() ]

#solution 1
print('solution1',blinkvec(stonelist,25))

#solution 2
sol2 = blinkvec(stonelist,75)
print('solution2',sol2)