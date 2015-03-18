import csv

with open('richness_fishbase_family.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('richness_fishbase_family.csv', mode='w') as outfile:
    writer = csv.writer(outfile)
    for rows in reader:
        k = rows[0]
        v = rows[1]
        mydict = {k:v for k, v in rows}
    print(mydict)
#does not print what i want
#could not figure out what went wrong
