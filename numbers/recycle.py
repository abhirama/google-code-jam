import pprint
import itertools
import sys

def areSame(no0, no1):
    ln = len(no0) 
    con = ln
    end = 1
    while con:
        if (no1[-end:] + no1[0:(ln - end)]) == no0:
            return True 
        con = con - 1
        end = end + 1

    return False

lines = sys.stdin.readlines()

prntFormat = u'Case #{0}: {1}';

case = 1
for line in lines[1:]:
    line = line.strip()
    bounds = line.split()
    dct = {}


    low = long(bounds[0])
    high = long(bounds[1]) + 1

    for no in xrange(low, high):
        lst = [i for i in str(no)]
        lst.sort()
        st = ''.join(lst)

        if st in dct:
            dct[st].append(str(no))
        else:
            dct[st] = [str(no)]

    count = 0
    for nos in dct.values():
        if len(nos) > 1:
            combs = itertools.combinations(nos, 2)
            for pair in combs:
                (no0, no1) = pair
                if len(no0) == 2:
                    count = count + 1
                else:
                    if areSame(no0, no1):
                        count = count + 1
                 
    print prntFormat.format(case, count) 
    case = case + 1
