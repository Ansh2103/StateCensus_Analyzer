import pytest

from Main_CensusAnalyzer.CensusAnalyser_Exception import WrongFilePathError, WrongExtensionFile, WrongDelimiterFile

INDIA_STATE_CENSUS_CSV_PATH = '../IndianStateCensusAnalyzer/Main_CensusAnalyzer/IndiaStateCensusData.csv'
WRONG_INDIA_STATE_CSV_FILE = '../IndianStateCensusAnalyzer/test_CensusAnalyzer/IndiaStateCensusData.csv'
WRONG_FILE_TYPE = '../IndianStateCensusAnalyzer/Main_CensusAnalyzer/IndiaStateCensusData.json'
DELIMITER_CENSUS_DATA = '../IndianStateCensusAnalyzer/Main_CensusAnalyzer/delimeter_census_data.csv'
WRONG_DELIMITER_PATH = '../IndianStateCensusAnalyzer/test_CensusAnalyzer/delimeter_census_data.csv'
WRONG_HEADER_PATH = '../IndianStateCensusAnalyzer/test_CensusAnalyzer/MissingHeader_StateCensusData.csv'
INDIA_STATE_CODE_PATH = '../IndianStateCensusAnalyzer/Main_CensusAnalyzer/IndiaStateCode.csv'
WRONG__STATE_CODE_CSV_PATH = '../IndianStateCensusAnalyzer/test_StateCensusAnalyzer/IndiaStateCode.csv'
WRONG_STATE_CODE_FILE_TYPE = '../IndianStateCensusAnalyzer/StateCensusAnalyser/IndiaStateCode.json'


def test_load_census_data(instance_of_main_class):
    number_of_records = instance_of_main_class.load_census_data(INDIA_STATE_CENSUS_CSV_PATH)
    assert number_of_records == 28


def test_wrong_filepath(instance_of_main_class):
    with pytest.raises(WrongFilePathError):
        instance_of_main_class.load_census_data(WRONG_INDIA_STATE_CSV_FILE)


def test_file_type(instance_of_main_class):
    with pytest.raises(WrongExtensionFile):
        instance_of_main_class.load_census_data(WRONG_FILE_TYPE)

def test_load_census_delimiter_data(instance_of_main_class):
    number_of_records = instance_of_main_class.load_census_delimiter_data(DELIMITER_CENSUS_DATA)
    assert number_of_records == 28


def test_wrong_delimiter_filepath(instance_of_main_class):
    with pytest.raises(WrongFilePathError):
        instance_of_main_class.load_census_data(WRONG_DELIMITER_PATH)


def test_wrong_header_filepath(instance_of_main_class):
    with pytest.raises(WrongFilePathError):
        instance_of_main_class.load_census_data(WRONG_HEADER_PATH)


def test_load_census_code_data(instance_of_main_class):
    number_of_records = instance_of_main_class.load_census_data(INDIA_STATE_CODE_PATH)
    assert number_of_records == 36


def test_wrong_state_census_code_filepath(instance_of_main_class):
    with pytest.raises(WrongFilePathError):
        instance_of_main_class.load_census_data(WRONG__STATE_CODE_CSV_PATH)


def test_wrong_state_code_file_type(instance_of_main_class):
    with pytest.raises(WrongExtensionFile):
        instance_of_main_class.load_census_data(WRONG_STATE_CODE_FILE_TYPE)
