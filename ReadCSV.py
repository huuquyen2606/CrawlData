import csv
import collections
columns = collections.defaultdict(list)
with open('dataLink.csv', 'r',encoding="utf8") as file:
    reader = csv.reader(file)
    i = 0
    for row in reader:
        i+=1
        for (k,v) in enumerate(row):
            columns[k].append(v)

        if i==5: break
    print(columns[1])