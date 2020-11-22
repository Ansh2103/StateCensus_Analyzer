import pytest

from Main_CensusAnalyzer.CensusAnalyser_Exception import WrongFilePathError, WrongExtensionFile

INDIA_STATE_CENSUS_PATH = '/home/shubh/PycharmProjects/IndianStateCensusAnalyzer/Main_CensusAnalyzer/IndiaStateCensusData.csv'
WRONG_CSV_PATH = '/home/shubh/PycharmProjects/test_UserRegistration/IndiaStateCensusData.csv'
WRONG_FILE_EXTENSION = '/home/shubh/PycharmProjects/StateCensusAnalyzer/StateCensusAnalyser/IndiaStateCensusData.json'
INDIA_STATE_CODE_PATH = '/home/shubh/PycharmProjects/IndianStateCensusAnalyzer/Main_CensusAnalyzer/IndiaStateCode.csv'
WRONG__STATE_CODE_CSV_PATH = '/home/shubh/PycharmProjects/StateCensusAnalyzer/test_StateCensusAnalyzer/IndiaStateCode.csv'
WRONG_STATE_CODE_FILE_EXTENSION = '/home/shubh/PycharmProjects/StateCensusAnalyzer/StateCensusAnalyser/IndiaStateCode.json'


def test_load_census_data(instance_of_main_class):
    count_of_entries = instance_of_main_class.load_census_data(INDIA_STATE_CENSUS_PATH)
    assert count_of_entries == 28