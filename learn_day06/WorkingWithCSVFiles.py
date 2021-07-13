#open the file in text mode
import csv
file_path = "/RISHI/H2K/FileIO/CSVFilesteachers.csv"
file_path_write = "/RISHI/H2K/FileIO/CSVTest.csv"
with open(file_path, "rt") as file:
    '''
    for eachRow in file:
        print(eachRow, type(eachRow))
    '''
    # data = csv.reader(file)
    data = csv.DictReader(file)
    for eachRowData in data:
        print(eachRowData, type(eachRowData))

    file.close()

print("Done")

#open the CSV file
with open(file_path_write, mode='w') as file:
    data = csv.writer(file)

    #write data to the file, row by row
    data.writerow(['Login email', 'Identifier', 'First name', 'Last name'])
    data.writerow(['laura@example.com', '2070', 'Laura', 'Grey'])
    data.writerow(['craig@example.com', '4081', 'Craig', 'Johnson'])
    data.writerow(['mary@example.com', '9346', 'Mary', 'Jenkins'])
    data.writerow(['jamie@example.com', '5079', 'Jamie', 'Smith'])
    file.close()

print("Writing Done")