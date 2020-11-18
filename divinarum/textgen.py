# !python 3.7.4
import lorem   # to generate initial message


class TextGenerator:
    """
    generates a random sentence from lorem ipsum
    """

    @staticmethod
    def generate_lorem():
        text = lorem.sentence()
        return text
