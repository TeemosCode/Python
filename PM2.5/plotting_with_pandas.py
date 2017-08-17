#plotting with pandas
import matplotlib.pyplot as plt
import pandas as pd
data = [[3,22,18], [22,3,6], [13,6,14]]
index = ["Teemo", "Trist", "Urgot"]
columns = ["Kills", "Deaths", "Assists"]
df = pd.DataFrame(data, columns = columns, index = index)
df.plot() ###blingblinglblinggg
plt.show()