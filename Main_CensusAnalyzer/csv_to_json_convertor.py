import json
import csv

#conversion of IndiaStateCensusData.csv to IndiaStateCensusData.json

with open("IndiaStateCensusData.csv", "r") as csv_file :
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    data = {"india_state_census_data": []}
    for line in csv_reader:
        data["india_state_census_data"].append({"State": line[0], "Population": line[1],
                                                "AreaInSqKm": line[2], "DensityPerSqKm": line[3]})

with open("IndiaStateCode.csv","w") as json_file:
    json.dump(data,json_file,indent=4)


#conversion of IndiaStateCode.csv to IndiaStateCode.json

with open("IndiaStateCode.csv", "r") as csv_file :
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    data = {"india_state_code": []}
    for line in csv_reader:
        data["india_state_code"].append({"SrNo":line[0],"State Name":line[1],
                                                "TIN":line[2],"StateCode":line[3]})

with open("IndiaStateCode.json","w") as json_file:
    json.dump(data,json_file,indent=4)

