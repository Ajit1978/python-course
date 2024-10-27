nameList = [ "Amit", "Ajay", "Atul", "Amol", "Bhola", "Bhim", "Ramesh", "Rakesh", "Sandesh", "Vighnesh"]
print(nameList)
print(nameList[9])


if "Raja" in nameList:
    print("name exist")
else: 
    print("name not exist")

print(nameList[2:7])

nameList[2]="Sanket"
print(nameList)

nameList.append("sammer")
nameList.insert(4, "navin")

print(nameList)