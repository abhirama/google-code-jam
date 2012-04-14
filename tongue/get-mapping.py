import pprint

examples = {
     "a zoo" : "y qee",
     "ejp mysljylc kd kxveddknmc re jsicpdrysi" : "our language is impossible to understand",
     "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" : "there are twenty six factorial possibilities",
     "de kr kd eoya kw aej tysr re ujdr lkgc jv" : "so it is okay if you want to just give up"
}

code = {}

for ori, mapping in examples.iteritems():
    for a, b in zip(ori, mapping):
        code[a] = b

pprint.pprint(code)

