import csv
def readd():
    with open('readd.csv', newline='') as in_file, open('out_readd.txt', 'w') as out_file:
        spamreader = csv.reader(in_file, delimiter=',', quotechar='"')
        num = 0
        key = ''
        for row in spamreader:
            line = "\"%s\",%s,\"%s\"" % (row[0],row[1],row[2])
            num += 1
            if num%2 == 1:
                key = row[0]
            else:
                line = copy(row,key)
            out_file.write(line)
            out_file.write('\n')
def copy(row, key):
    print("key is %s" % key)
    raws = row[2].split(';')
    raws[0] = key
    return "\"%s\",%s,\"%s\"" % (row[0],row[1],';'.join(raws))

readd()