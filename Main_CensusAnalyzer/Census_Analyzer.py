import csv
import logging
import re

from Main_CensusAnalyzer.CensusAnalyser_Exception import WrongFilePathError,WrongExtensionFile

class CensusAnalyser:
    logging.basicConfig( filename='new_census_analyser.log',level=logging.DEBUG,
                         format='%(name)s | %(levelname)s | %(asctime)s | %(message)s')

    census_list = []

    def check_extension(self, csv_file_path):

        FILE_REGEX = '.*.csv$'
        pattern = re.compile(FILE_REGEX)
        match = pattern.search(csv_file_path)
        if not match:
            logging.error(' There is an incorrect extension i.e; exception occured ')
            raise WrongExtensionFile(' Please provide a valid csv file')

    def load_census_data(self, csv_file_path):

        self.check_extension(csv_file_path)
        try:
            with open(csv_file_path, 'r') as census_data:
                for line in csv.DictReader(census_data):
                    self.census_list.append(line)
                count = len(self.census_list)
                logging.debug('Number of entries {}'.format(count - 1))
        except FileNotFoundError:
            logging.exception('File Path Error Exception,Incorrect File Path Input ')
            raise WrongFilePathError('Please provide valid file path')
        return count - 1
