# With Array of Data
sample_data = [1,2,3,4,5,6,7,8,9]
name = "H2KInfosys Inc."
'''
for eachValue in dataSet:
    Operation on eachValue
'''
total = 0
for eachSample in sample_data:
    print(eachSample)
    total = total + eachSample
print("Total", total)

for eachChara in name:
    print(eachChara)

# with range function - range(start, end, step)
total = 0
for eachValue in range(0, 11, 2):
    print(eachValue)
    total = total + eachValue
print("New Total", total)


for eachStep in range(100, 90, -1):
    print(eachStep)


# Reverse a String with For Loop
# Reverse a String in one line statement