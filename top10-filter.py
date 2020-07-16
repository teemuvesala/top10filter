#!/usr/bin/env python3
import csv
import sys
import os

file = sys.argv[1]
with open(file) as file:
    reader = csv.reader(file, delimiter=',')

    first = reader.__next__()
    labels = []
    samples = []
    for smpl in first[1:]:
        samples.append({ 'name' : smpl, 'count' : {} })
    for line in reader:
        label = line[0]
        labels.append(label)
        index = 0
        for count in line[1:]:
            samples[index]['count'][label] = int(count)
            index = index + 1

for sample in samples:
    sorted_sample =  sorted(sample['count'].items(), key=lambda x: x[1], reverse=True)
    sample['count'] = dict(sorted_sample)
    for key in list(sample['count'].keys())[10:]:
        sample['count'][key] = 0

header = ','.join([str(d['name']) for d in samples])
print(f',{header}')
for item in labels:
    results = ','.join([str(d['count'][item]) for d in samples])
    print(f'{item},{results}')

