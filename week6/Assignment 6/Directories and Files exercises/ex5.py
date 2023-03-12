mylist = ['a', 'b','c', 'd']
with open('list.txt', "w") as textf:
        for c in mylist:
                textf.write("%s\n" % c)
content = open('list.txt')

print(content.read())