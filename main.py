from src.parser import parser
from src.create_deck import create_deck
import os


def main():

    while True:

        file_name = input(
            'Please specify from which file you would like to generate flash'
            'cards\n(Press "q" to quit.)\n>>> '
        )
        if file_name == 'q':
            return False

        while True:
            is_grammar = input(
                'Do you want to add some grammatical expressions? (y/n)'
                '\n(Press "q" to quit.)\n>>> '
            )
            if is_grammar == 'y':
                is_grammar = True
                break
            elif is_grammar == 'n':
                is_grammar = False
                break
            else:
                print(
                    'Please try again. ("y" for "yes and "n" for "no")'
                    '\n(Press "q" to quit.)\n>>> '
                )
        xml_files = os.scandir(path='./data/xml_files')
        path_to_xml = f"./data/xml_files/{file_name}"

        exists = False
        for entry in xml_files:
            if entry.path == path_to_xml:
                exists = True

        if exists is False:
            print(
                'No file with this name exists\n'
                'Please try again\n(Press "q" to quit.)\n>>> '
            )

        vocab = parser(path_to_xml)
        create_deck(vocab, file_name, is_grammar)
        print('Flashcard created!\n--------------\n')


if __name__ == '__main__':
    main()
