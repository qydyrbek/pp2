def gensquares(n):
    for i in range(n):
        yield i**2
        
for x in gensquares(int(input())):
    print(x)
