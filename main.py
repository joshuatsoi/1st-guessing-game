import getpass

number_to_guess = getpass.getpass("Enter a number between (1-5): ")

user_guess = input("Your guess: ")

print(f'The answer is {number_to_guess}')

if user_guess == number_to_guess:
    print('You guessed correct!!!!!!!!!')
elif user_guess > number_to_guess:
    print("Your guess is too high!")
else:
    print('Your guess is too low')    

