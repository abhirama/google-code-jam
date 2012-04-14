import pprint
import itertools
import sys
import time

start = time.time()

def helper(no, lowBnd, hgBnd):
    ln = len(no)
    con = ln
    end = 1

    lst = [long(no)]

    while con > 1:
        genNo = long(no[-end:] + no[0:(ln - end)])
        if (genNo >= lowBnd) and (genNo < hgBnd) and (genNo not in lst):
            lst.append(genNo)
        con = con - 1
        end = end + 1

    count = 0
    for comb in itertools.combinations(lst, 2):
        count = count + 1    

    return (count, lst)


lines = sys.stdin.readlines()

prntFormat = u'Case #{0}: {1}';

case = 1
for line in lines[1:]:
    line = line.strip()
    bounds = line.split()
    seen = {}

    low = long(bounds[0])
    high = long(bounds[1]) + 1

    count = 0
    for no in xrange(low, high):
        strNo = str(no)
        lst = [i for i in strNo]
        lst.sort()
        st = ''.join(lst)

        if st in seen:
            if no not in seen[st]:
                retCount, lst = helper(strNo, low, high)
                count = retCount + count
                seen[st] = seen[st] + lst
        else:
            retCount, lst = helper(strNo, low, high)
            count = retCount + count
            seen[st] = lst 

    print prntFormat.format(case, count) 
    case = case + 1

print time.time() - start
