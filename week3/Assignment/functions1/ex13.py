import random
number = random.randint(1,20)
name =input("Hello, What's your name?")
cnt = 0
print('Well, ' + name + ' I am thinking of a number between 1 and 20.')
while cnt < 5:
    guess=int(input())
    cnt = cnt + 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(cnt) + ' tries!')
else:
    print('You did not guess the number,The number was '+ str(number))