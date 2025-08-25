# !python 3.11.13
import random
from divinarum.reader import Reader


class NameGenerator:

    """
    generates a silly random first and last name for the rival from a long list of names
    """

    words_file = open(Reader.get_file_path(Reader.namegen_sources_dir), "r")

    word_obj = words_file.read()
    words = word_obj.split()

    upper_words = [word for word in words if word[0].isupper()]
    name_words = [word for word in upper_words if not word.isupper()]

    @staticmethod
    def rand_name():
        char_name = ' '.\
            join([NameGenerator.name_words[random.randint(1, len(NameGenerator.name_words))] for i in range(2)])
        return char_name
