import sys

lines = sys.stdin.readlines()
cnt = int(lines[0].strip())

opFormat = u"Case #{0}: {1}"

for no, line in enumerate(lines[1:]):
    line = line.strip()

    cont = line.split()

    surTrip = int(cont[1])

    p = int(cont[2])

    count = 0
    for score in cont[3:]:
        score = int(score)
        if score == 0:
            if p == 0:
                count = count + 1
        else :
            if score >= ((p * 3) - 4):
                if (score / 3) >= p:
                    count = count + 1
                else:
                    dif = (p * 3) - score
                    if dif <= 2:
                        count = count + 1
                    if (dif > 2) and surTrip:
                        surTrip = surTrip - 1
                        count = count + 1

    print opFormat.format(no + 1, count)

        
        
        
