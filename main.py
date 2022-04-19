import time, requests, random
import pandas as pd
from os import system, name

score = 0


def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


csv = pd.read_csv('pokemon.csv')

print('Welcome to the pokemon type guessing game.')
time.sleep(0.5)
print('type "quit" to quit the game')

game_should_continue = True

while game_should_continue:
    random_pokemon = csv.loc[random.randint(0, 1045)]
    name = random_pokemon['name']
    correct_answer = random_pokemon['type']
    answer = input(f'Current Score: {score}\nGuess the type of: {name}\n').title()

    if answer == correct_answer:
        score += 1
        print(f'You are right. Score:{score}')
        time.sleep(1)

    elif answer == 'quit':
        game_should_continue = False
    else:
        print(f'You are wrong. the correct answer was {correct_answer}. Score:{score}')
        time.sleep(2.5)
    clear()
