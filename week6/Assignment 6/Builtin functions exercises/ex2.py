def counter(string):
    up_cnt = 0
    low_cnt = 0
    for x in string:
        if x.isupper():
            up_cnt += 1
        elif x.islower():
            low_cnt += 1
    return up_cnt, low_cnt


lyric = "Seniń baiaý qozǵalǵanyń unaidy Týra qaraǵanyń unaidy, dál solai"
upper, lower = counter(lyric)
print(upper) 
print(lower) 
