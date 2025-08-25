# !python 3.11.13
from divinarum.ai import AI
from divinarum.textgen import TextGenerator
from divinarum.crypt import Crypt
from divinarum.namegen import NameGenerator
import random
import time  # to print text gradually
import sys


class GameMaster:

    """
    to randomly generate stuff and tell the story/outcome(s)
    """

    desired_number = None  # number to guess for both participants
    max_rounds = None  # after reaching that point the game will suddenly be over; known to GM only
    lower_border = None  # lower border for AI guessing
    upper_border = None  # upper border for AI guessing
    crypt_key = None  # the key used for en/decrypting the message
    coded_message = None

    # INT METHODS

    @staticmethod
    def generate_random_int(start, end):

        random_int = random.randint(start, end)

        return random_int

    @staticmethod
    def generate_lower_border(difficulty):

        if difficulty in ['a', 'A']:
            GameMaster.lower_border = GameMaster.generate_random_int(1, 5)
        elif difficulty in ['b', 'B']:
            GameMaster.lower_border = GameMaster.generate_random_int(1, 4)
        elif difficulty in ['c', 'C']:
            GameMaster.lower_border = GameMaster.generate_random_int(1, 3)

        return GameMaster.lower_border

    @staticmethod
    def generate_upper_border(difficulty):

        if difficulty in ['a', 'A']:
            GameMaster.upper_border = GameMaster.generate_random_int(10, 20)
        elif difficulty in ['b', 'B']:
            GameMaster.upper_border = GameMaster.generate_random_int(30, 40)
        elif difficulty in ['c', 'C']:
            GameMaster.upper_border = GameMaster.generate_random_int(50, 60)

        return GameMaster.upper_border

    @staticmethod
    def generate_desired_number(lower_border, upper_border):

        desired_number = GameMaster.generate_random_int(lower_border, upper_border)

        return desired_number

    @staticmethod
    def generate_max_rounds(difficulty):
        # the higher the difficulty, the fewer guessing attempts can players have

        if difficulty in ['a', 'A']:
            GameMaster.max_rounds = GameMaster.generate_random_int(15, 20)
        elif difficulty in ['b', 'B']:
            GameMaster.max_rounds = GameMaster.generate_random_int(10, 15)
        elif difficulty in ['c', 'C']:
            GameMaster.max_rounds = GameMaster.generate_random_int(5, 10)

        return GameMaster.max_rounds

    @staticmethod
    def generate_crypt_key(number):

        if number < 26:
            GameMaster.crypt_key = number
        elif number >= 26:
            GameMaster.crypt_key = int(number/3)  # since max guessing number is 60

        return GameMaster.crypt_key

    # STRING METHODS

    @staticmethod
    def print_dots():
        width = 3
        times = 3

        for i in range(times):
            for j in range(width):
                time.sleep(0.8)
                sys.stdout.write(".")
            sys.stdout.write("\r")
            sys.stdout.flush()
        sys.stdout.write("\n")
        print()

    @staticmethod
    def introduce_situation():

        # should probably put the text into json and then read it with the reader class, idk

        sentences = [
            {
                "Lately, the Hermetic Order, which you happen to be a part of,": 1,
                "received a strange message said to contain a prophecy about the Order's future.": 1,
                "Unfortunately, no one could interpret it properly to this moment.": 1,
             },
            {
                "As one of the Order's prominent members, you think that this may be your big chance,": 2,
                "since you are highly skilled at divination,": 2,
                "having practiced spells of this school for years.": 2,
            },
            {
                "You could show your importance to the Order as well as advance in the Mages' ranks.": 3,
                "So, with great hope in heart, you enter the Order's secret temple, where the meetings take place.": 3,
            },
            {
                "However, as you walk into the splendidly decorated Main Hall,": 4,
                "you notice that you are not the only one to test your luck.": 4,
            },
            {
                "A wizard from a notorious rival magic school has also come to the challenge.": 5,
                "The Archmagister decides that the best option, since there are two candidates,": 5,
                "would be to organize several rounds, in which both of you will try do decipher the message.": 5,
            },
            {
                "The first to find the key correctly wins the contest and gets all the praise.": 6,
                "However, in order not to make this easy, the number of rounds will be decided based on your skill.": 6,
            },
            {
                "None of the contestants knows the exact number,": 7,
                "but since your skill level is pretty much the same as your rival's,": 7,
                "it won't bother you too much, you think.": 7,
            },
            {
                "To win in this contest, you need to correctly interpret the signs which the crystal ball shows.": 8,
                "Your rival will also try to decipher the same signs.": 8,
            }
        ]

        print()

        for sentence in sentences:
            for item in list(sentence):
                print(item)
            print()
            GameMaster.print_dots()

    @staticmethod
    def generate_opponents_desc():
        # randomly choosing the opponents' description from a predefined list

        opponent_descs_list = [', a skilled elderly wizard.', ', a middle-aged power-hungry magician.',
                               ', a young aspiring mage.']
        desc = random.choice(opponent_descs_list)

        return desc

    @staticmethod
    def introduce_opponent():

        AI.name = NameGenerator.rand_name()
        AI.description = GameMaster.generate_opponents_desc()
        print('Your opponent is ' + AI.name + AI.description)

    @staticmethod
    def generate_message():

        number = GameMaster.generate_crypt_key(GameMaster.desired_number)
        text = TextGenerator.generate_lorem()
        GameMaster.coded_message = Crypt.caesar_cipher(number, text, encrypted=False)

        return GameMaster.coded_message

    @staticmethod
    def decipher_message():

        decoded_message = Crypt.caesar_cipher(GameMaster.crypt_key, GameMaster.coded_message, encrypted=True)

        return decoded_message

    @staticmethod
    def show_game_intro():

        sentences = [
            {
                "To decipher the message you use an old technique - scrying with the crystal ball.": 1,
                "So both of you, aided by the Archmagister, have come to the ritual chamber.": 1,
            },
            {
                "On an intricately carved oaken table stands the crystal ball.": 2,
                "It is glowing with shimmering light.": 2,
            },
            {
                "While you are looking at it, the clouds outside the temple,": 3,
                "permeating through the opulent stained glass paintings on the gothic windows,": 3,
                "reflect in the ball in strange shapes.": 3,
            },
            {
                "In the center of the ball appears something that looks like a number,": 4,
                "but it cannot be seen clearly.": 4,
            },
        ]

        print()

        for sentence in sentences:
            for item in list(sentence):
                print(item)
            print()
            GameMaster.print_dots()

        print('It looks like something in between ' + str(GameMaster.lower_border) +
              ' and ' + str(GameMaster.upper_border) + '.')

    @staticmethod
    def show_victory_message():

        print("You managed to crack the code. Now the Archmagister will decipher the message.")
        print()
        print("The original message was as follows:")
        print(GameMaster.decipher_message())

    @staticmethod
    def show_loss_message():

        print("Unfortunately, your opponent got hold of the cipher key first.")
        print("Only the Gods know what the key is going to be used for...")
