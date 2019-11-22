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
    return new
