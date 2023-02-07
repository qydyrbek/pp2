a = input()
x =a.count('f')
if x==1 :
    print (a.find('f'))
elif x>1 :
    print(a.find('f'), a.rfind('f'))