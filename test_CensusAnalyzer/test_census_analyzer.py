import pytest

from Main_CensusAnalyzer.CensusAnalyser_Exception import WrongFilePathError, WrongExtensionFile

INDIA_STATE_CENSUS_PATH = '/home/shubh/PycharmProjects/IndianStateCensusAnalyzer/Main_CensusAnalyzer/IndiaStateCensusData.csv'

def test_load_census_data(instance_of_main_class):
    count_of_entries = instance_of_main_class.load_census_data(INDIA_STATE_CENSUS_PATH)
    assert count_of_entries == 28