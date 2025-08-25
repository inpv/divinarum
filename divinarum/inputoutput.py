# !python 3.11.13
import os


class InputOutput:

    """
    controls player input
    """

    player_answer = ""
    player_name = ""
    difficulty = None  # the difficulty level of the game

    @staticmethod
    def request_anykey():

        InputOutput.player_answer = input("Type a key and hit Enter,")

        return InputOutput.player_answer

    @staticmethod
    def handle_general_exception():

        if InputOutput.player_answer not in ['g', 'G', 'y', 'y', 'l', 'L', 'y', 'Y', 'n', 'N']:
            print("Not a valid answer, try again.")
            print()
        else:
            InputOutput.request_anykey()

    @staticmethod
    def ask_name():

        print()
        print("Please enter your name:")
        InputOutput.player_name = input()

        while len(str(InputOutput.player_name)) <= 2:
            print("Your character should have a sensible name. Please chose one:")
            InputOutput.player_name = input()

        return InputOutput.player_name

    @staticmethod
    def ask_difficulty():

        print()
        print("How deep is your understanding of the paranormal?")
        print()
        print("a - What is paranormal?")
        print("b - I can read the signs.")
        print("c - I know everything about this game already.")
        print()
        print("Choose one:")
        InputOutput.difficulty = input()

        return InputOutput.difficulty

    @staticmethod
    def ask_for_quit():

        while True:
            print("Do you really want to quit? (y or n?):")
            InputOutput.player_answer = input()

            if InputOutput.player_answer in ['y', 'Y', 'yes', 'Yes', 'YES']:
                print("Quitting..")
                exit(0)
            elif InputOutput.player_answer in ['n', 'N', 'no', 'No', 'NO']:
                print("Fine, let's return to divination.")
                print()
                break
            else:
                print("Not a valid answer, try again.")
                print()
                continue

    @staticmethod
    def clear():
        # for windows
        if os.name == 'nt':
            os.system('cls')
            # for mac and linux(here, os.name is 'posix')
        else:
            os.system('clear')

