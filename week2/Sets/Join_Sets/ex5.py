myset = {"kok", 'tok', 'sok', 'sok'}
ekinshi = {'yt', 'jazz', 'alyp meni', 'tok'}

ushinshi = myset.intersection(ekinshi)
print(ushinshi)

ekinshi.symmetric_difference_update(myset)
print(ekinshi)