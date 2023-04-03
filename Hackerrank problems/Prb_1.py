def trp(limit):
    triples = []
    for a in range(1, limit):
        for b in range(a,limit):
            c = (a**2 + b**2)**0.5
            if c == int(c) and c <limit:
                triples.append((a,b,int(c)))
    return triples
    
# print(trp(20))
for triples in sorted(trp(20)):
    print("{} {} {}".format(triples[0],triples[1],triples[2]))