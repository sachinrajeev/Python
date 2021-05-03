#!/usr/bin/env python3
import sys
import csv
import math

file1_name = sys.argv[1]
file2_name = sys.argv[2]

person1 = {}
person2 = {}

metrics = {
    'ankle': ['ankle_left', 'ankle_right', ],
    'hip': ['hip_right', 'hip_left', ],
    'knee': ['knee_left', 'knee_right', ],
    'shoulder': ['shoulder_right', 'shoulder_left', ],
    'elbow': ['elbow_left', 'elbow_right', ],
    'wrist': ['wrist_left', 'wrist_right', ],
    'head': ['chin', 'forehead', ],
}


def get_diff(point1, point2):
    return math.sqrt((point1['x'] - point2['x'])**2 + (point1['y'] - point2['y'])**2)


with open(file1_name, 'r') as file1:
    reader = csv.reader(file1)
    for row in reader:
        if row:
            if row[0] == 'position':
                continue
            person1[row[0]] = {
                'x': float(row[1]),
                'y': float(row[2]),
            }

with open(file2_name, 'r') as file2:
    reader = csv.reader(file2)
    for row in reader:
        if row:
            if row[0] == 'position':
                continue
            person2[row[0]] = {
                'x': float(row[1]),
                'y': float(row[2]),
            }

print(person1)
person1_metrics = {}
person2_metrics = {}

max_diff = 0
for metric, metric_vals in metrics.items():
	person1_metrics[metric] = get_diff(person1[metric_vals[0]], person1[metric_vals[1]])
	person2_metrics[metric] = get_diff(person2[metric_vals[0]], person2[metric_vals[1]])
	diff = abs(person1_metrics[metric] - person2_metrics[metric])
	if max_diff < diff:
		max_diff = diff

if (max_diff < 100):
	print("Yes")
else:
    print("No")
print(max_diff)
