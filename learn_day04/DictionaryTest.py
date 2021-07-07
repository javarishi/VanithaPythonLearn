# Dictionaries are written in Curly Braces { "Key" : "value"}

sampleDictionary = {
    "101" : "Cuberland Store",
    102 : "Alpharetta Store",
    "103" : "Duluth Store",
    104: "Vinning Street"
}
# Accessing Items: sampleDictionary["101"]
print(sampleDictionary["101"])
# Access with Get: sampleDictionary.get("102")
print(sampleDictionary.get("102"))
# Add key value pair: sampleDictionary["104"] = "NewItem"
sampleDictionary["105"] = "Macon Store"
print(sampleDictionary)
sampleDictionary[104] = "Vinning Street Store"
print(sampleDictionary)
# Iterate Keys: for eachKey in sampleDictionary:
for eachKey in sampleDictionary:
    print(eachKey,sampleDictionary.get(eachKey))
#Iterate Key, Value : for key, value in sampleDictionary.items():

for key,value in sampleDictionary.items():
    print(key, value)

# Iterate  just Value : for eachValue in sampleDictionary.values()
for eachValue in sampleDictionary.values():
    print(eachValue)

# Check Key Exists? if "101" in sampleDictionary:

# Check Value Exists? if "item" in sampleDictionary.values():
if "Macon Store" in sampleDictionary.values():
    print("Value exists")
# Remove Item with Key: sampleDictionary.pop("101")

# Remove Last Added Item: sampleDictionary.popitem()
sampleDictionary.popitem()
print("sampleDictionary.popitem()", sampleDictionary)

# Check Length: len(sampleDictionary)
print(len(sampleDictionary))