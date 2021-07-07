
# Sets are written with curly brackets
sampleSet = {"apples", "oranges", "bananas"}
# Add Element: sampleSet.add("mango")
sampleSet.add("mango")
print("add ", sampleSet)
# Does not allow Duplicates
sampleSet.add("mango")
print("Does not allow Duplicates ", sampleSet)
# Iterate: for eachItem in sampleSet:
for eachItem in sampleSet:
    print(eachItem)
# Element Exists? : if "apple" in sampleSet:

# Add another set: sampleSet.update(anotherSet)
anotherSet = {"tomatos", "potatos", "apples"}
sampleSet.update(anotherSet)
print("update ", sampleSet)
# Check Length: len(sampleSet)

# Remove Element: sampleSet.remove("banana") - gives error if element doesnt exists
'''
sampleSet.remove("apples")
print("discard ", sampleSet)
sampleSet.remove("apples") # Simply Ignore
print("discard ", sampleSet) '''
# Discard (No Error) : sampleSet.discard("apple") -ignores if element doest exists
sampleSet.discard("apples")
print("discard ", sampleSet)
sampleSet.discard("apples") # Simply Ignore
print("discard ", sampleSet)

# Clear Set: sampleSet.clear()