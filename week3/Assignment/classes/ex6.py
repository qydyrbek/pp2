def func(n):
    for i in range(2,n,1):
        if n%i==0:
            return False

    return True

n = input().split()
prime = list(filter(lambda x : func(int(x)) , n))
print(prime)