a = int(input())
def fib(x):
    if x == 1 or x == 2:
        return 1
    elif x == 0:
        return 0
    else:
        return fib(x - 1) + fib(x - 2)

print(fib(a))
