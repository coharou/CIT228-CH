import math
import matplotlib.pyplot as plt

values = [1, 2, 3, 4, 5]
second = []
third = []
for i in values:
    second.append(math.pow(i, 2))
    third.append(math.pow(i, 3))

plt.subplot(1, 2, 1)
plt.plot(second, marker='+', ls='')

plt.title("Second Power", color="blue", fontfamily="Times New Roman", fontsize="13")
plt.xlabel("Power", color="blue", fontfamily="Times New Roman", fontsize="12")
plt.ylabel("Output", color="blue", fontfamily="Times New Roman", fontsize="12")

plt.style.use('fivethirtyeight')
plt.subplot(1, 2, 2)
plt.plot(third, marker='o', color='red', lw = '2.0', ls = '--')

plt.title("Third Power", color="blue", fontfamily="Times New Roman", fontsize="13")
plt.xlabel("Power", color="blue", fontfamily="Times New Roman", fontsize="12")
plt.ylabel("Output", color="blue", fontfamily="Times New Roman", fontsize="12")

plt.subplots_adjust(wspace=1)
plt.suptitle("Main Charts", color="blue", fontfamily="Times New Roman", fontsize="16")
plt.show()
