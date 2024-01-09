import csv
data = []

with open("dwarf_stars.csv") as f:
    csvReader = csv.reader(f)

    for row in csvReader:
        data.append(row)

header = data[0]

stars_data = data[1:]

for row in stars_data:
    row[1] = row[1].lower()

stars_data.sort(key = lambda stars_data: stars_data[1]) 

with open("dwarf_Stars_sorted.csv", "w", newline = "") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(header)
    csvWriter.writerows(stars_data)