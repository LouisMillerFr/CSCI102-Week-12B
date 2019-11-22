# https://github.com/LouisMillerFr/CSCI102-Week-12B
# Louis Miller
# CSCI 102 - Section A
# Week 11 - Part B

def PrintOutput(s): print(f'OUTPUT {s}')

def LoadFile(file):
    f = open(file,"r")
    l = f.readlines()
    f.close()
    for i in range(len(l)): l[i].replace('\n', '')
    return l

def UpdateString(old, rep, loc):
    new = ''
    for i in range(len(old)):
        if i == loc: new += rep
        else: new += old[i]
    PrintOutput(new)

def FindWordCount(l, word):
    num = 0
    for i in range(len(l)):
        if l[i] == word: num += 1
    return num

def ScoreFinder(l1, l2, string):
    for i in range(len(l1)):
        l1[i] = l1[i].lower()
    if string.lower() in l1:
        n = 0
        while l1[n].lower() != string.lower():
            n += 1
        PrintOutput(f'Jill got a score of {l2[n]}')
    else: PrintOutput('player not found')

def Union(l1, l2): return (l1 + l2)

def Intersection(l1, l2):
    l = []
    for i in range(len(l1)):
        if l1[i] in l2:
            l.append(l1[i])
    return l

def NotIn(l1, l2):
    l = []
    for i in range(len(l1)):
        if l1[i] not in l2:
            l.append(l1[i])
    return l
