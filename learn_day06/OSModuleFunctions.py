import os

file_path = "/RISHI/H2K/FileIO/CSVFilesteachers1.csv"
file_path_write = "/RISHI/H2K/FileIO/CSVTest.csv"

if os.path.exists(file_path):
    print("File exists at ", file_path)
else:
    print("File NOT exists at ", file_path)

file_dir = file_path = "/RISHI/H2K/FileIO"

for eachFile in os.listdir(file_dir):
    print(eachFile)
    if 'demofile.txt' in eachFile:
        os.mkdir("/RISHI/H2K/FileIO/Demo")
