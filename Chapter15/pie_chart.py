import matplotlib.pyplot as plt  

img_format = ['PNG', 'JPG', 'SVG', 'GIF', 'Other']
loc_count = [376, 348, 153, 104, 19]

colors = ('red', 'blue', 'yellow', 'purple', 'green')
explode = (0.4, 0, 0, 0, 0)

plt.pie(loc_count, explode = explode, labels = img_format, autopct = '%2.1f%%', shadow = True, startangle = 90, colors = colors)

plt.title('Usage of Image Formats by Websites')

plt.show()