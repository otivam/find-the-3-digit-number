import random

print('Welcome to my game! Please try to guess the 3 digit number.')

#Generating 3 random digits
digits = list(range(10))
random.shuffle(digits)
random_numbs = (digits[:3])
print(random_numbs)

#Some game logic goes here
#Close
def close(num):
    counter = 0
    for x in num:
        if (x in random_numbs):
            counter = counter + 1
    if counter > 0:
        return True
    else:
        return False

#Match
def match(num):
    for x in range(len(random_numbs)):
        if num[0] == random_numbs[0] or num[1] == random_numbs[1] or num[2] == random_numbs[2]:
            return True
        else:
            return False

#Nope
def nope(num):
    counter = 0
    for x in num:
        if x in random_numbs:
            counter = counter + 1
    if counter == 0:
        return True
    else:
        return False


#Win
def win(num):
    result = []
    for x in num:
        result.append(x)
    return result

#winning condition
while (True):
    #Getting the user's input
    answer = input("What is your guess?")
    guess = [int(x) for x in str(answer)]
    print(guess)

    if win(guess) == random_numbs:
        print('You have won!')
        break
    if match(guess) and not (win(guess) == random_numbs):
        print("You've guessed a correct number in the correct position.")
    if close(guess) and not match(guess):
        print("You've guessed a correct number but in the wrong position.")
    if nope(guess):
        print("You haven't guess any of the numbers correctly.")
