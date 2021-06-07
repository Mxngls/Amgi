import csv
from parse_xml import Parser

class Converter:

     def create_csv(file):

          vocab, file_name = Parser().parse_xml(file)

          with open(f"{file_name.replace('xml', 'csv')}", 'w') as csvfile:
               filewriter = csv.writer(csvfile, delimiter=',',
                              quotechar='|', quoting=csv.QUOTE_MINIMAL)
               fields = ['id', 'subjectCategory', 'vocabularyLevel', 'word',
                        'sense_id', 'translation', 'definition', 'krDefintion', 'example']
               filewriter.writerow(fields)

               for word in vocab:
                    filewriter.writerow([word[0]['id'], word[0]['subjectCategory'], word[0]['vocabularyLevel'],
                                         word[0]['hangul'], word[1][0]['sense_id'], word[1][0]['translation'],
                                         word[1][0]['definition'], word[1][0]['krDefintion'], word[1][0]['example']])

