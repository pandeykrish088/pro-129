import csv
import pandas as pd

file1 = "bright_stars_sorted.csv"
file2 = "dwarf_Stars_sorted.csv"

data1 = []
data2 = []

with open(file1, "r", encoding = "utf8") as b:
    csvReader = csv.reader(b)

    for row in csvReader:
        data1.append(row)

with open(file2, "r", encoding = "utf8") as b:
    csvReader = csv.reader(b)

    for row in csvReader:
        data2.append(row)

header1 = data1[0]
header2 = data2[0]

dwarf_stars = data1[1:]
bright_stars = data2[1:]

header = header1 + header2
data = []

for i in dwarf_stars:
    data.append(i)

for k in bright_stars:
    data.append(k)

with open("merged_dataset.csv", "w", encoding = "utf8") as m:
    csvWriter = csv.writer(m)
    csvWriter.writerow(header)
    csvWriter.writerows(data)

df = pd.read_csv("merged_dataset.csv")