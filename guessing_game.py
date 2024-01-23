''' A four-digit guessing game.
This game gives you 10 chances to guess a four-digit computer generated game. just type in your guess and it will tell how many numbers are found in their correct place and incorrect place in each round.
The uses the command line interface for interaction
'''
import random

def four_digit_guess():
    list_1 = []
    for digit in range(4):
        digit = random.randint(0, 9)
        list_1.append(str(digit))
    target = ''.join(list_1)
    
    print('You have 10 chances to guess a randomly generated number using the info provided.')
    guess = input('Guess a number: ')
    while len(guess) != 4:
        guess = input('Type a 4-digit number.\nGuess a number: ')
    count = 1
    
    while guess != target:
        correct_place = 0
        incorrect_place = 0
        tempo = target
        for i in range(4):
            if guess[i] == target[i]:
                correct_place += 1
                tempo = tempo.replace(guess[i], '')
        for i in range(4):
            if guess[i] in tempo:
                incorrect_place += 1
                tempo = tempo.replace(guess[i], '')
        print(
            f'Number guessed right and in the correct place: {correct_place}')
        print(
            f'Number guessed right but not in correct place: {incorrect_place}')
        guess = input('Guess again: ')
        while len(guess) != 4:
            guess = input('Type a 4-digit number.\nGuess again: ')
        count += 1
        
        if count == 10:
            print(f'Sorry! you did not find it. the number was {target}.')
            break   
        
        print(f'Congratulations you found the number! you took {count} guesses')

if __name__ == '__main__':
    four_digit_guess()
