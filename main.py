from random import random
import math

class Die:
    FACES: list[str] = [
        "┌─────────┐\n│         │\n│    •    │\n│         │\n└─────────┘",
        "┌─────────┐\n│ •       │\n│         │\n│       • │\n└─────────┘",
        "┌─────────┐\n│ •       │\n│    •    │\n│       • │\n└─────────┘",
        "┌─────────┐\n│ •     • │\n│         │\n│ •     • │\n└─────────┘",
        "┌─────────┐\n│ •     • │\n│    •    │\n│ •     • │\n└─────────┘",
        "┌─────────┐\n│ •     • │\n│ •     • │\n│ •     • │\n└─────────┘"
    ]

    def __init__(self, sides: int) -> None:
        self.sides = sides

    def roll_once(self) -> int:
        return math.floor(random() * self.sides) + 1
    
    def roll_many(self, times: int) -> list[int]:
        return [self.roll_once() for roll in range(times)]

def main():

    die = Die(6)
    print("Enter 'quit' to exit the loop")
    while True:
        user_input = input('How many dices would you like to roll ? ')

        if user_input == 'quit':
            break

        if user_input.isdigit():
            dices = die.roll_many(int(user_input))
            output = ''
            for i in range(5):
                for dice in dices:
                    stringify_dice = die.FACES[dice - 1]
                    output += stringify_dice.splitlines()[i] + ' '
                output += '\n'
            print(f'{output} The total is {sum(dices)}, the mean is {sum(dices)/len(dices)}')
        else:
            print('Not a number, please enter a number')

if __name__ == '__main__':
    main()