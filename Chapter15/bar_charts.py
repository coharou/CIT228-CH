import matplotlib.pyplot as plt  
import numpy as np 

# percentage of fast food consumption per day by different sexes and age groups    
# https://www.cdc.gov/nchs/data/databriefs/db322_table.pdf#page=1

men = [37.9,46.5,37.6,25.6]
women = [35.4,43.3,37.8,22.7]
total = [36.6,44.9,37.7,24.1]

age_range=["Over 20","20-39","40-59","Over 60"]

w = 0.1

mBar = np.arange(len(age_range))
wBar = [i + w for i in mBar]
tBar = [i + w for i in wBar]

plt.bar(mBar, men, color = 'orange', width = w, label = 'Men')
plt.bar(wBar, women, color = 'red', width = w, label = 'Women')
plt.bar(tBar, total, color = 'green', width = w, label = 'Total')

plt.xticks([e + w for e in range(len(age_range))], age_range)

plt.legend(loc = 'lower right', ncol = 1, fontsize = 10)

plt.title('Percentage of Fast Food Consumption vs. Age')

plt.xlabel('Age Groups')
plt.ylabel("Percentage of Adults Consuming Fast Food / day")

plt.show() 