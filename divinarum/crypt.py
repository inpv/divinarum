# !python 3.11.13
import string  # to generate the alphabet


class Crypt:
    """
    encrypts and decrypts the message
    """

    @staticmethod
    def caesar_cipher(shift, text, encrypted):

        if not encrypted:
            pass
        elif encrypted:
            shift = 26 - shift  # move by 26 symbols to decrypt

        alpha_lower = string.ascii_lowercase  # loading lowercase letters
        alpha_upper = string.ascii_uppercase  # loading uppercase letters

        # moving each alphabet according to the shift value
        shifted_alphabet_lower = alpha_lower[shift:] + alpha_lower[:shift]
        shifted_alphabet_upper = alpha_upper[shift:] + alpha_upper[:shift]

        alphabet = alpha_lower + alpha_upper  # joining the alphabets into one
        shifted_alphabet = shifted_alphabet_lower + shifted_alphabet_upper  # the shifted as well

        table = str.maketrans(alphabet, shifted_alphabet)  # creating a mapping table

        coded_text = text.translate(table)  # code the text according to the table

        return coded_text
