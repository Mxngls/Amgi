from src.parser import parser
from src.create_csv import create_csv
from src.create_deck import create_deck
import os


def main():

    while True:

        file_name = input(
            'Please specify from which file you would like to generate flash'
            ' cards\n(Press "q" to quit.)\n>>> '
        )
        if file_name == 'q':
            return False

        xml_files = os.scandir(path='./data/xml_files')
        path_to_xml = f"./data/xml_files/{file_name}"

        exists = False
        for entry in xml_files:
            if entry.path == path_to_xml:
                exists = True
                break
        if exists is False:
            print(
                'No file with this name exists\n'
                'Please try again\n(Press "q" to quit.)\n>>> '
            )

        vocab = parser(path_to_xml)
        create_deck(vocab, file_name)
        print('Flashcard created!\n--------------\n')


if __name__ == '__main__':
    main()
