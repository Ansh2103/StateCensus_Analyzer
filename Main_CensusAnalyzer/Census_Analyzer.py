import csv
import logging
import re

from Main_CensusAnalyzer.CensusAnalyser_Exception import WrongFilePathError , WrongExtensionFile , WrongDelimiterFile
logging.basicConfig( filename='new_census_analyser.log',level=logging.DEBUG,
                         format='%(name)s | %(levelname)s | %(asctime)s | %(message)s')
class CensusAnalyser:


    def check_extension(self, csv_file_path):

        FILE_REGEX = '.*.csv$'
        pattern = re.compile(FILE_REGEX)
        validate = pattern.search(csv_file_path)
        if not validate:
            logging.error(' Exception occurred due to wrong file extension',)
            raise WrongExtensionFile(' Please provide a valid csv file')

    def load_census_data(self, csv_file_path):

        self.check_extension(csv_file_path)
        try:
            with open(csv_file_path, 'r') as census_file:
                csv_reader = csv.DictReader(census_file)
                next(csv_reader)
                count = len(list(csv_reader))
                logging.debug('Number of records: {}'.format(count))

        except FileNotFoundError:
            logging.exception('File Path Error Exception,Incorrect File Path Input ')
            raise WrongFilePathError('Please provide valid file path')

        return count

    def load_census_delimiter_data(self, csv_file_path):

        self.check_extension(csv_file_path)
        try:
            with open(csv_file_path, 'r') as census_file:
                csv_reader = csv.DictReader(census_file)
                next(csv_reader)
                count = len(list(csv_reader))
                logging.debug('Number of records: {}'.format(count))

        except FileNotFoundError:
            logging.exception('File Path Error Exception,Incorrect File Path Input ')
            raise WrongDelimiterFile('Please provide valid file path')
        return count


