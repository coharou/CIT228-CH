import json
import math
import matplotlib.pyplot as plt

with open('Chapter16/readable_all_day.json') as f:
    data = json.load(f)

data_dict = data['features']

magnitudes = []
for feature in data_dict:
    magnitude = feature['properties']['mag']
    magnitudes.append(magnitude)

txt_ranges = ['< 1', '1', '2', '3', '4', '5']
ranges = [0, 0, 0, 0, 0, 0]
for m in magnitudes:
    mag = int(math.floor(m))
    if m < 1:
        ranges[0] += 1
    if m >= 1 and m < 2:
        ranges[1] += 1
    if m >= 2 and m < 3:
        ranges[2] += 1
    if m >= 3 and m < 4:
        ranges[3] += 1
    if m >= 4 and m < 5:
        ranges[4] += 1
    if m >= 5:
        ranges[5] += 1

plt.title('Number of Earthquakes by Magnitude on March 22nd, 2021')
plt.pie(ranges, labels = txt_ranges, autopct = '%2.0f%%')
plt.show()