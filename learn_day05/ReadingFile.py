
file_path = "/RISHI/H2K/FileIO/demofile.txt"
'''
Modes of file
r = read only -default
w - write - wipe out existing file and start fresh
a - append 
x - create
w -x - a - creates the file if not exits

t - test
b - binary
'''

file = open(file_path, "rt")
# print(file.read())

for eachrow in file:
    print(eachrow)

file.close()