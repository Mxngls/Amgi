from src.parse_xml import parse_xml
from src.create_csv import create_csv
from src.create_deck import create_deck

def main():

        xml_input = input('Please specify from which file you would like to generate flash cards\n')
        path_to_xml = f"data/xml_files/{xml_input}"
        vocab, file_name = parse_xml(path_to_xml)
        csv = create_csv(vocab, file_name)
        create_deck(csv)
        print('Deck created!')

if __name__ == '__main__':
    main()