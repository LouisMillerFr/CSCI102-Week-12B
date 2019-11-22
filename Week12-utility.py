def PrintOutput(s): print(f'OUTPUT {s}')

def LoadFile(file):
    f = open(file,"r")
    l = f.readlines()
    for i in range(len(l)): l[i].replace('/n', '')
    return l

def UpdateString(old, rep, loc):
    new = ''
    for i in range(len(old)):
        if i == loc: new += rep
        else: new += old[i]
    PrintOutput(new)

def FindWordCount(file, word):
    num = 0
    l = file.readlines()
    for i in range(len(l)): l[i].replace('/n', '')
    for i in range(len(l)):
        if l[i] == word: num += 1
    return num

def ScoreFinder(l1, l2, string):
    if string in l1:
        n = 0
        while l1[n].lower() != string.lower():
            n += 1
        PrintOutput(f'Jill got a score of {l2[n]}')
    else: PrintOutput('player not found')

def Union(l1, l2): return (l1 + l2)


