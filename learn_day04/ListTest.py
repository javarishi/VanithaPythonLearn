# Lists are written with square brackets.
sampleList = ["apples", "oranges", "bananas"]


# Access Items: sampleList[1]
print(sampleList[1])

# Add Element: sampleList.append("newItem")
sampleList.append("grapes")
print("append :: ", sampleList)
# Allows Duplicates
sampleList.append("grapes")
print("Allows Duplicates :: ", sampleList)
# Add Indexed Element: sampleList.insert(1, "fruits")
sampleList.insert(1, "pineapples")
print("insert :: ", sampleList)
# Remove Element: sampleList.remove("item")
sampleList.remove("bananas")
print("remove :: ", sampleList)
# Remove Indexed Element: sampleList.pop(1)
sampleList.pop(1)
print("pop :: ", sampleList)
# Using Delete function: del sampleList[0]
# del sampleList[0]
# Check the Length: len(sampleList)
print("length :: ", len(sampleList))
# Iterate: for eachItem in sampleList:
for eachItem in sampleList:
    print(eachItem)
# Element Exists? : if "apple" in sampleList:
if "apples" in sampleList:
    print("apples is in list")
# Sorting: sampleList.sort()
sampleList.sort()
print("sort", sampleList)
# Clear List: sampleList.clear()
# sampleList.clear()
sampleList.clear()
print("clear", sampleList)