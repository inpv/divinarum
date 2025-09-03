# !python 3.11.13
from divinarum.textgen import TextGenerator
from divinarum.crypt import Crypt
from divinarum.reader import Reader
import random


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
    name = ''  # opponent's name
    description = ''  # opponent's desc


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
    def generate_desc_from_json_by_key(key):

        # should probably put the text into json and then read it with the reader class, idk
        # AAANNND, DONE!

        print()
        Reader.print_json_by_key(key, path=Reader.json_data_dir)

        if key == "show_game_intro":
            print('It looks like something in between ' + str(GameMaster.lower_border) +
                  ' and ' + str(GameMaster.upper_border) + '.')
        elif key == "introduce_situation":
            pass

    @staticmethod
    def generate_opponents_action():
        rival_guess_replies = \
            ['Your rival reaches his hands to the crystal ball and starts muttering some incomprehensible gibberish...',
             'Your rival draws a sigil in the air to see the insides of the ball more clearly...',
             'Your rival stares into the ball blankly for quite some time...']
        action = random.choice(rival_guess_replies)
        return action

    @staticmethod
    def generate_opponents_response():
        opponent_response_list = ['You will never defeat me.', 'Your skills are worthless compared to mine.',
                                  'Looks like the arcane arts are not for you.']
        taunt = random.choice(opponent_response_list)
        resp = "[" + str(GameMaster.name) + "]:" + " " + taunt
        return resp

    @staticmethod
    def generate_opponents_desc():
        # randomly choosing the opponents' description from a predefined list

        opponent_descs_list = [', a skilled elderly wizard.', ', a middle-aged power-hungry magician.',
                               ', a young aspiring mage.']
        desc = random.choice(opponent_descs_list)

        return desc

    @staticmethod
    def generate_rand_name():
        """
        generates a silly random first and last name for the rival from a long list of names
        """

        words_file = open(Reader.get_file_path(Reader.namegen_sources_dir), "r")

        word_obj = words_file.read()
        words = word_obj.split()

        upper_words = [word for word in words if word[0].isupper()]
        name_words = [word for word in upper_words if not word.isupper()]
        char_name = ' '. \
            join([name_words[random.randint(1, len(name_words))] for i in range(2)])
        return char_name

    @staticmethod
    def introduce_opponent():

        GameMaster.name = GameMaster.generate_rand_name()
        GameMaster.description = GameMaster.generate_opponents_desc()
        print('Your opponent is ' + GameMaster.name + GameMaster.description)

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
    def show_victory_message():

        print("You managed to crack the code. Now the Archmagister will decipher the message.")
        print()
        print("The original message was as follows:")
        print(GameMaster.decipher_message())

    @staticmethod
    def show_loss_message():

        print("Unfortunately, your opponent got hold of the cipher key first.")
        print("Only the Gods know what the key is going to be used for...")
