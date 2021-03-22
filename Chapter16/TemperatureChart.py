import csv
import matplotlib.pyplot as plt

dates = []
highs = []
lows = []

with open('Chapter16/2515906.csv') as f:
    r = csv.reader(f, delimiter = ',')
    for l in r:
        if l[3] != '':
            if l[4] != '':
                dates.append(l[2])
                highs.append(int(l[3]))
                lows.append(int(l[4]))
                
days = range(len(dates))

plt.scatter(days, lows, color = 'blue', label = 'Lows')
plt.scatter(days, highs, color = 'orange', label = 'Highs')

plt.suptitle('Temperatures in Grosse Pointe Shores From January 1950 to October 1950')
plt.title('Low Temperatures vs. High Temperatures')

plt.legend(loc = 'lower right', ncol = 2, fontsize = 16)

plt.show()