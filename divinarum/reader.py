# !python 3.7.4
import os
import sys


class Reader:
    """
    reads the text from included files
    """

    license_dir = "txt_files\\license.txt"
    namegen_sources_dir = "txt_files\\namegen_sources.txt"

    @staticmethod
    def get_file_path(rel_path):
        # used to get the actual path to included files when bundling the app into a single .exe
        # i.e. with PyInstaller

        if getattr(sys, "frozen", False):
            # If the 'frozen' flag is set, we are in bundled-app mode
            file_path = os.path.abspath(os.path.join(sys._MEIPASS, rel_path))
        else:
            # Normal development mode. Use os.getcwd() or __file__ as appropriate in your case...
            file_path = os.path.abspath(os.path.join(os.getcwd(), rel_path))

        return file_path

    @staticmethod
    def read_text_file(file_name):
        file = open(file_name, "r")
        print(file.read())

        print()
        exit_var = input("Type a key and press Enter to exit to the main menu: ")
        print()

        del [exit_var]
