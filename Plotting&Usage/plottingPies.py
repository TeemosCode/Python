import matplotlib.pyplot as plt

labels = ["East", "South", "North", "Mid"]
sizes = [5, 10, 20, 15]
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0, 0.05, 0)
plt.pie(sizes, explode = explode, labels = labels, colors = colors, labeldistance = 1.1, \
	autopct = "%3.1f%%", shadow = True, startangle = 90, pctdistance = 0.6)

plt.axis("equal") #make it round instead of the default which is oval
plt.legend()
plt.show()
