import pytest

from Main_CensusAnalyzer.CensusAnalyser_Exception import WrongFilePathError, WrongExtensionFile

INDIA_STATE_CENSUS_PATH = '/home/shubh/PycharmProjects/IndianStateCensusAnalyzer/Main_CensusAnalyzer/IndiaStateCensusData.csv'
WRONG_CSV_FILE = '/home/shubh/PycharmProjects/test_UserRegistration/IndiaStateCensusData.csv'
WRONG_FILE_TYPE = '/home/shubh/PycharmProjects/IndianStateCensusAnalyzer/Main_CensusAnalyzer/IndiaStateCensusData.json'

def test_load_census_data(instance_of_main_class):
    count_of_entries = instance_of_main_class.load_census_data(INDIA_STATE_CENSUS_PATH)
    assert count_of_entries == 28

def test_wrong_filepath(instance_of_main_class):
    with pytest.raises(WrongFilePathError):
        instance_of_main_class.load_census_data(WRONG_CSV_FILE)

def test_file_type(instance_of_main_class):
    with pytest.raises(WrongExtensionFile):
        instance_of_main_class.load_census_data(WRONG_FILE_TYPE)
