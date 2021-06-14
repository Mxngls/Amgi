import csv
     
def create_csv(vocab, file_name):

     with open(f"{file_name.replace('xml', 'csv')}", 'w') as csvfile:
          # Create a CSV-file with the rows specifed in the fields parameter.
          filewriter = csv.writer(csvfile, delimiter=',',
                         quotechar='|', quoting=csv.QUOTE_MINIMAL)
          fields = ['id', 'subjectCategory', 'vocabularyLevel', 'word',
                   'sense_id', 'translation', 'definition', 'krDefintion', 'example']
          filewriter.writerow(fields)

          # An index for the different Senses.
          SenseIndex = ['a', 'b', 'c', 'd']

          # Populate the created CSV-file.
          for word in vocab:
               if len(word[1]) > 1:
                    for i, Sense in enumerate(word[1]):
                         filewriter.writerow([word[0]['id'], word[0]['subjectCategory'], word[0]['vocabularyLevel'],
                                              f"<span>{word[0]['hangul']}<sup style='font-size: 75%'>{SenseIndex[i]}</sup></span>", 
                                              word[1][i]['sense_id'], word[1][i]['translation'],
                                              word[1][i]['definition'], word[1][i]['krDefintion'], word[1][i]['example']])
                         if i > 2:
                              break
               else:
                    filewriter.writerow([word[0]['id'], word[0]['subjectCategory'], word[0]['vocabularyLevel'],
                                         word[0]['hangul'], word[1][0]['sense_id'], word[1][0]['translation'],
                                         word[1][0]['definition'], word[1][0]['krDefintion'], word[1][0]['example']])

     return file_name.replace('xml', 'csv')
     