import csv


with open('IndiaStateCensusData.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('delimeter_census_data.csv','w') as new_file:
        field_names = ['State','Population','AreaInSqKm','DensityPerSqKm']
        csv_writer = csv.DictWriter(new_file,fieldnames=field_names, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)


with open('IndiaStateCode.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('delimeter_census_code_data.csv','w') as new_file:
        field_names = ['SrNo','State Name','TIN','StateCode']
        csv_writer = csv.DictWriter(new_file,fieldnames=field_names, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)