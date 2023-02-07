s = str(input())
a = s.find('h')
b = s.rfind('h')
print(s[:(a + 1)] + s[(b - 1): a: -1] + s[b:])