# !python 3.11.13
import os
import sys
import time
import json

class Reader:
    """
    reads the text from included files
    """

    license_dir = "divinarum/txt_files/license.txt"
    namegen_sources_dir = "divinarum/txt_files/namegen_sources.txt"
    json_data_dir = "divinarum/data/texts.json"

    # HELPER METHODS

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
    def print_dots():
        width = 3
        times = 3

        for i in range(times):
            for j in range(width):
                time.sleep(0.5)
                sys.stdout.write(".")
            sys.stdout.write("\r")
            sys.stdout.flush()
        sys.stdout.write("\n")
        print()

    # PARSING METHODS

    @staticmethod
    def read_text_file(file_name):
        file = open(file_name, "r")
        print(file.read())

        print()
        exit_var = input("Type a key and press Enter to exit to the main menu: ")
        print()

        del [exit_var]

    @staticmethod
    def load_json(path: str):
        """
        Read and parse JSON, returning the raw parsed structure.
        If path is None, fall back to default file in the class variable.
        """
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def print_json_by_key(*keys, path):
        data = Reader.load_json(path)
        # assume `data` is a dict: key -> list of lists of strings
        if keys:
            target = keys
        else:
            target = tuple(data.keys())

        for k in target:
            sentences = data.get(k, [])
            for sentence in sentences:
                for item in sentence:
                    print(item)
                print()
                Reader.print_dots()