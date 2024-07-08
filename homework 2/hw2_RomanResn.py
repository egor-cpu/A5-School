typeOfNumberr = input("ISBN-10 or ISBN-13 ")

if "ISBN-10" or "ISBN-13" not in typeOfNumberr:
    print("Non correct input data")

ISBN = input("Input ISBN: ")

arrayOfSymbolsISBN = []
for i in range(len(ISBN)):
    arrayOfSymbolsISBN.append(int(ISBN[i]))

arrayOfSymbolsISBN.reverse()

count = 0
index = 0

for j in range(2, int(typeOfNumberr[5:]) + 1):
    count += arrayOfSymbolsISBN[index] * j
    index += 1
devide = count % 11 
if (11 - devide) == arrayOfSymbolsISBN[0]:
    print("Number is Valid")
elif (11 - devide) == 10:
    print("Number is Valid (with X)")
else:
    print("Number is not Valid")