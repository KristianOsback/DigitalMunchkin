import csv
import time
from collections import defaultdict

columns = defaultdict(list)

with (open('MunchkinTreasureCards.csv', "r"), delimiter=",") as f:
    reader = csv.reader(f)
    reader.next()
    for row in reader:
        for (i,v) in enumerate(row):
            columns[i].append(v)
            b=(columns[2])

            for x in b[:]:
                with open('file2.csv') as f, open('file3.csv', 'a') as g:
                    reader = csv.reader(f)
                    #next(reader, None) # discard the header
                    writer = csv.writer(g)
                    for row in reader:
                        if row[2] == x:
                            writer.writerow(row[:2])