import pandas as pd

#building dataframe
df = pd.DataFrame({"teemo": [3,22,18], "trist": [22,3,6], "urgot": [13,6,14]})
# or
data = [[3,22,18], [22,3,6], [13,6,14]]
index = ["Teemo", "Trist", "Urgot"]
columns = ["Kills", "Deaths", "Assists"]
df = pd.DataFrame(data, columns = columns, index = index)
#changing the attributes of the data frame
#df.columns = new_col    df.index = new_index
index[0] = "TEETO"
df.index = index
columns[2] = [3,3,3]
df.columns = columns


#getting data of data frame COLUMNS
#df["column_name"]
df["Kills"]
# if needed more than 1 COLUMNS of data, need to pass a list of lists --> ([ [ ] ])
df[["Kills", "Deaths"]]
#it could also contain logic during the choosing process of the data frame
#df[df.attribute > x]
df[df.Kills >= 10]

df.values # acquires ALL data, represented in a 2 dimensional list [[]]
df.values[0] # here, we are getting TEETO's KDA (data)
df.values[0][1] # getting TEETO's Deaths data value

