number = 10
guesses_made = 0

print('I\'m thinking of a number...')
guess = input('What number am I thinking of? ')
guesses_made += 1

while True:
    if guesses_made == 5:
        print(f'You are out of guesses! The number was {number}')
        break
    if guess == str(number):
        print(('Congratulations! You guessed the right number.'))
        break
    elif guess == 'q':
        print(f'The number was {number}.')
        break
    else:
        if int(guess) > number:
            guess = input(f'Too high! try again ({5 - guesses_made} tries left). ')
            guesses_made += 1
        elif int(guess) < number:
            guess = input(f'Too low! try again ({5 - guesses_made} tries left). ')
            guesses_made += 1