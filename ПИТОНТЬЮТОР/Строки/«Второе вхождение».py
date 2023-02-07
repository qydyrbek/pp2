s = input()
count = s.count('f')
if count == 0:
    print(-2)
elif count == 1:
    print (-1)
else:
    c = s.find('f')
    c = s.replace('f',' ',1)
    print(c.find('f'))