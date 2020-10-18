import csv

def getCsvFile(fileName):
    rows = []
    dataFile = open(fileName, "r")
    reader = csv.reader(dataFile)
    #skip the headers
    next(reader)
    for row in reader:
        rows.append(row)

    return rows


