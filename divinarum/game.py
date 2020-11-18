# !python 3.7.4

import random
from divinarum.menu import Menu
from divinarum.gm import GameMaster
from divinarum.player import Player
from divinarum.ai import AI
from divinarum.reader import Reader
from divinarum.inputoutput import InputOutput


class Game:
    """
    the game flow
    """

    round_number = 0
    intro_shown = False

    # INITIALIZING GAME CLASS INSTANCES

    io_interface = InputOutput()  # handles the button presses
    game_player = Player()  # data for player
    game_ai = AI()  # our (not so)dumb enemy
    game_files_reader = Reader()  # text files' parser
    main_menu = Menu()  # the start screen and the menu
    game_master = GameMaster()  # sets the game conditions and tells the story

    @staticmethod
    def run_game():

        # TITLE SCREEN

        Game.main_menu.show_title()
        Game.io_interface.request_anykey()
        Game.io_interface.clear()

        # MAIN GAME LOOP

        while True:

            Game.main_menu.show_menu()
            Game.io_interface.request_anykey()

            # MENU CHOICES

            if InputOutput.player_answer in ['g', 'G']:

                Game.io_interface.clear()

                # ASKING THE PLAYER THE PARAMS USED IN THE GAME
                Game.io_interface.ask_name()
                Game.io_interface.ask_difficulty()

                # GENERATE MAXIMUM ROUNDS NUMBER BASED ON DIFFICULTY
                Game.game_master.generate_max_rounds(InputOutput.difficulty)

                # CHECK IF THE PLAYER WANTS TO SKIP THE INTRO

                while Game.intro_shown:
                    print('Do you want to skip the intro? (y/n)')
                    InputOutput.player_answer = input()
                    print()

                    # SKIPPING THE INTRO (OR NOT)
                    if InputOutput.player_answer in ['y', 'y']:
                        break
                    elif InputOutput.player_answer in ['n', 'N']:
                        Game.game_master.introduce_situation()
                        break
                    else:
                        InputOutput.handle_general_exception()
                else:
                    Game.game_master.introduce_situation()

                # GAME INTRO SHOWN
                Game.intro_shown = True

                # GENERATING A RANDOM OPPONENT FOR THE PLAYER
                Game.game_master.introduce_opponent()

                # GENERATING DATA FOR THE GAME
                # borders based on difficulty
                Game.game_master.generate_lower_border(InputOutput.difficulty)
                Game.game_master.generate_upper_border(InputOutput.difficulty)
                # the number to guess
                GameMaster.desired_number = \
                    Game.game_master.generate_desired_number(GameMaster.lower_border, GameMaster.upper_border)
                # the encrypted message
                print()
                print("The message that was received is as follows:")
                print(str(Game.game_master.generate_message()))

                print()
                # here change the question to "would you like to go on?", if not - exit to menu
                Game.io_interface.request_anykey()

                # THE INTRO FOR EACH GAME
                Game.game_master.show_game_intro()

                # THE ROUND STARTS

                while Game.round_number <= GameMaster.max_rounds:
                    print()
                    print('Starting round ' + '№' + str(Game.round_number+1) + '...')

                    # HUMAN GUESSING BLOCK
                    print('Concentrate on your powers and take a guess...')
                    guessed_human_number = input()
                    print()
                    print('Your guess is ' + str(guessed_human_number) + '.')
                    print()

                    # AI GUESSING BLOCK
                    print('Now your opponent takes a guess!')
                    guessed_ai_number = Game.game_ai.guess_number_randomly(GameMaster.lower_border,
                                                                           GameMaster.upper_border)
                    print(Game.game_ai.generate_opponents_action())
                    print("Your opponent's guess is " + str(guessed_ai_number) + '.')
                    print()

                    # MAX ROUNDS LIMITS CALCULATION

                    if Game.round_number == GameMaster.max_rounds:
                        Game.round_number = 0  # clearing the rounds count
                        print("You've exceeded the time limits for the code to reveal itself.")
                        print("You should try next time.")
                        print()
                        break
                    else:
                        Game.round_number += 1

                    # SHOWING THE RESULTS

                    # in case the player won
                    if int(guessed_human_number) == GameMaster.desired_number and guessed_ai_number != \
                            GameMaster.desired_number:
                        print("Congratulations, " + str(InputOutput.player_name) + "! " +
                              "You won the game. Flawless victory over " + str(AI.name) + ".")  # move to gm?
                        print()
                        GameMaster.show_victory_message()
                        Game.round_number = 0  # clearing the rounds count
                        print()
                        break

                    # in case it's a draw
                    elif int(guessed_human_number) == GameMaster.desired_number and guessed_ai_number == \
                            GameMaster.desired_number:
                        print("It's a draw. Take another turn? (y/n)")

                    # in case the player lost
                    elif int(guessed_human_number) != GameMaster.desired_number and guessed_ai_number == \
                            GameMaster.desired_number:
                        print('You lost to your opponent.')
                        print(AI.generate_opponents_response())
                        print()
                        GameMaster.show_loss_message()
                        Game.round_number = 0  # clearing the rounds count
                        print()
                        break

                    # in case both player and ai guessed wrong
                    elif int(guessed_human_number) != GameMaster.desired_number and guessed_ai_number != \
                            GameMaster.desired_number:
                        print('No one of you guessed right. Take another turn? (y/n)')

                    # CHECK WHETHER PLAYER WANTS ANOTHER TURN
                    InputOutput.player_answer = input()

                    if InputOutput.player_answer in ['y', 'Y']:
                        pass
                    elif InputOutput.player_answer in ['n', 'N']:
                        Game.round_number = 0  # clearing the rounds count
                        break
                    else:
                        InputOutput.handle_general_exception()

            elif InputOutput.player_answer in ['l', 'L']:
                Game.io_interface.clear()
                Game.game_files_reader.read_text_file(Reader.get_file_path(Reader.license_dir))
                Game.io_interface.clear()

            elif InputOutput.player_answer in ['q', 'Q']:
                Game.io_interface.clear()
                Game.io_interface.ask_for_quit()

            else:
                Game.io_interface.handle_general_exception()
                Game.io_interface.clear()
