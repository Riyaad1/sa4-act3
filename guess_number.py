number = 10

print('I\'m thinking of a number...')
guess = input('What number am I thinking of? ')

while True:
    if guess == str(number):
        print(('Congratulations! You guessed the right number.'))
        break
    if guess == 'q':
        print(f'The number was {number}.')
        break
    else:
        if int(guess) > number:
            guess = input('Too high!, try again. ')
        elif int(guess) < number:
            guess = input('Too low! Try again. ')