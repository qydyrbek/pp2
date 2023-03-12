with open("textforex7.txt", 'r') as firstfile:
    with open("textforex7(2).txt", 'a') as secondfile:
        for line in firstfile:
            secondfile.write(line)
