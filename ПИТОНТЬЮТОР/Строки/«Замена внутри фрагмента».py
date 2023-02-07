s = input()
s = s.replace('h', 'H', s.count('h') - 1)
s = s.replace('H', 'h', 1)
print(s)
