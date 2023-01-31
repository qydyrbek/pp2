myset = {"kok", 'tok', 'sok', 'sok'}
ekinshi = {'yt', 'jazz', 'alyp meni', 'tok'}

ushinshi = myset.union(ekinshi)
print(ushinshi)

ekinshi.intersection_update(myset)
print(ekinshi)