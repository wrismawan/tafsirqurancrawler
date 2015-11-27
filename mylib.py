__author__ = 'wrismawan'
import csv

def CSV2List(filename):
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        new_list = list(reader)
    return new_list


def readFromCSV(filename):
    _file = open(filename)
    __file = open(filename)
    lines = csv.reader(_file)
    rows = csv.reader(__file)
    data = {}

    row_count = sum(1 for row in rows)
    data = [[] for i in range(row_count)]
    i = 0
    for row in lines:
        cells = row
        cols = len(cells)
        for cell in range(cols):
            if ('.' in cells[cell]):
                num = float(cells[cell])
            else:
                num = int(cells[cell])
            data[i].append(num)
        i += 1

    return data


def writeToCSV(listData, fileName):
    file_data = fileName
    with open(file_data, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        for i in listData:
            writer.writerow(i, )
    return file_data


def writeJSON(json, fileName):
    target = open(fileName, 'wb')
    target.write(json)
    return target


def readJSON(fileName):
    import json
    with open(fileName) as file:
        return json.load(file)

def JSON2Matrix(listInput):
    result = []
    for key, value in listInput.iteritems():
        l = [[key], value]
        row = [item for sublist in l for item in sublist]
        result.append(row)
    return result