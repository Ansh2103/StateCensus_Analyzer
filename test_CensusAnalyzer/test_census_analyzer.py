import pytest

from Main_CensusAnalyzer.CensusAnalyser_Exception import WrongFilePathError, WrongExtensionFile

INDIA_STATE_CENSUS_PATH = '/home/shubh/PycharmProjects/IndianStateCensusAnalyzer/Main_CensusAnalyzer/IndiaStateCensusData.csv'
WRONG_CSV_FILE = '/home/shubh/PycharmProjects/test_UserRegistration/IndiaStateCensusData.csv'
WRONG_FILE_TYPE = '/home/shubh/PycharmProjects/IndianStateCensusAnalyzer/Main_CensusAnalyzer/IndiaStateCensusData.json'
WRONG_DELIMITER_PATH = '/home/shubh/PycharmProjects/test_UserRegistration/delimeter_census_data.csv'
WRONG_HEADER_PATH = '/home/shubh/PycharmProjects/test_UserRegistration/MissingHeader_StateCensusData.csv'
INDIA_STATE_CODE_PATH = '/home/shubh/PycharmProjects/IndianStateCensusAnalyzer/Main_CensusAnalyzer/IndiaStateCode.csv'

def test_load_census_data(instance_of_main_class):
    number_of_records = instance_of_main_class.load_census_data(INDIA_STATE_CENSUS_PATH)
    assert number_of_records == 28

def test_wrong_filepath(instance_of_main_class):
    with pytest.raises(WrongFilePathError):
        instance_of_main_class.load_census_data(WRONG_CSV_FILE)

def test_file_type(instance_of_main_class):
    with pytest.raises(WrongExtensionFile):
        instance_of_main_class.load_census_data(WRONG_FILE_TYPE)

def test_wrong_delimiter_filepath(instance_of_main_class):
    with pytest.raises(WrongFilePathError):
        instance_of_main_class.load_census_data(WRONG_DELIMITER_PATH)

def test_wrong_header_filepath(instance_of_main_class):
    with pytest.raises(WrongFilePathError):
        instance_of_main_class.load_census_data(WRONG_HEADER_PATH)

def test_load_census_code_data(instance_of_main_class):
    number_of_records = instance_of_main_class.load_census_data(INDIA_STATE_CODE_PATH)
    assert number_of_records == 36
