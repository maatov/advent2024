import re

def load_input(fname):
    with open(fname,'rt') as f:
        data = f.read()
    return data


input = load_input('test-input.txt')
input = load_input('input.txt')

rgx = """mul\((\d{1,3}),(\d{1,3})\)"""
res = sum([int(mi[1])*int(mi[2]) for mi in re.finditer(rgx,input)])
print('solution1',res)
#do(),don't()
#split by do()
muls = 0
for ri in re.split("do\(\)",input):
    #split by don't()
    toeval = re.split("don't\(\)",ri)[0]
    muls += sum([int(mi[1])*int(mi[2]) for mi in re.finditer(rgx,toeval)])
print('solution2',muls)
