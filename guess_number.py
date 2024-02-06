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
        guess = input('Incorrect, try again. ')