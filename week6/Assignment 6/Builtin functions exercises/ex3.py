def f(x):
    x = x.replace(' ', '').lower()
    return x == x[::-1]

lyric = "Seniń baiaý qozǵalǵanyń unaidy Týra qaraǵanyń unaidy, dál solai"
if f(lyric):
    print("Yes")
else:
    print("No")
