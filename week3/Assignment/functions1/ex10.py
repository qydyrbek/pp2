def uni(l):
    x=[]
    for a in l:
        if a not in x:
            x.append(a)
    return x

print(uni([0,5,6,6]))