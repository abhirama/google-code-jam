import sys

code = {
 ' ': ' ',
 'a': 'y',
 'b': 'h',
 'c': 'e',
 'd': 's',
 'e': 'o',
 'f': 'c',
 'g': 'v',
 'h': 'x',
 'i': 'd',
 'j': 'u',
 'k': 'i',
 'l': 'g',
 'm': 'l',
 'n': 'b',
 'o': 'k',
 'p': 'r',
 'q': 'z',
 'r': 't',
 's': 'n',
 't': 'w',
 'u': 'j',
 'v': 'p',
 'w': 'f',
 'x': 'm',
 'y': 'a',
 'z': 'q'
}

lines = sys.stdin.readlines()

cnt = int(lines[0].strip())

opForamt = u"Case #{0}: {1}"
for no, line in enumerate(lines[1:]):
    line = line.strip()
    ori = ""
    for char in line:
        if char in code:
            ori = ori + code[char]
        else:
            ori = ori + char
    print opForamt.format(no + 1, ori)

    if no + 1 == cnt:
        break

