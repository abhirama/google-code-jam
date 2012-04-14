import pprint
import itertools
import sys
import time

start = time.time()

def helper(no, lowBnd, hgBnd):
    ln = len(no)
    con = ln
    end = 1

    mp = {long(no): 1}

    while con > 1:
        genNo = long(no[-end:] + no[0:(ln - end)])
        if (genNo >= lowBnd) and (genNo < hgBnd) and (genNo not in mp):
            mp[genNo] = 1
        con = con - 1
        end = end + 1

    count = 0
    for comb in itertools.combinations(mp.keys(), 2):
        count = count + 1    

    return (count, mp)


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
                retCount, mp = helper(strNo, low, high)
                count = retCount + count
                seen[st].update(mp)
        else:
            retCount, mp = helper(strNo, low, high)
            count = retCount + count
            seen[st] = mp 

    print prntFormat.format(case, count) 
    case = case + 1

print time.time() - start
