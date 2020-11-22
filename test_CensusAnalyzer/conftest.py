import pytest

from Main_CensusAnalyzer.Census_Analyzer import CensusAnalyser


@pytest.fixture
def instance_of_main_class():
    state_census_analyser =  CensusAnalyser()
    return state_census_analyser