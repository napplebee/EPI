import re

def find_11(s):
    r = "^(..)*11"
    r = "11(..)*$"
    #print "S", s
    count = 0
    try:
        while True:
            n = (re.search(r, s)).start()
            s = s[(n+2):]
            #print s
            count += 1
    except Exception as exc:
        #print exc
        return (count)

def num(char):
    if char == 'a':
        return 0
    if char == 'g':
        return 1
    if char == 't':
        return 2
    if char == 'c':
        return 3
    raise TypeError('not dna')

def check(np, nt, k):
    xor = bin(nt^np)
    res = xor.count('1') - find_11(xor)
    return (res ==k)

def find(k,p,t):
    np = 0
    nt = 0
    for i in range(len(p)):
        np = int(bin(np*4+num(p[i])),2)
        nt = int(bin(nt*4+num(t[i])),2)
    for i in range(len(p),len(t)):
        if check(np,nt,k):
            return (i-len(p))
        nt = int(bin((nt%(4**(len(p)-1)))*4+num(t[i])),2)
    if check(np, nt, k):
        return (len(t)-len(p))
    return None

k=2
p="cctg"
t="ccttacgactggt"
print (find(k,p,t))
