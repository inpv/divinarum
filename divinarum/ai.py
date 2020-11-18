# !python 3.7.4
import random


class AI:
    """
    generates a taunt from a list of taunts, also guesses randomly
    """

    name = ''  # opponent's name
    description = ''  # opponent's desc

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
        resp = "[" + str(AI.name) + "]:" + " " + taunt
        return resp

    @staticmethod
    def generate_random_int(start, end):
        random_int = random.randint(start, end)
        return random_int

    @staticmethod
    def guess_number_randomly(lower_border, upper_border):
        guessed = AI.generate_random_int(lower_border, upper_border)
        return guessed
