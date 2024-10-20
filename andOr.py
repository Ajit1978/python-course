age = int(input())
hasLicense = int(input())
if hasLicense==0:
    hasLicense=False
else:
    hasLicense=True

if (age>18 or hasLicense):
    print("Can Drive")
else:
    print("Can't drive")