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
# the down part of using the DataFrame "values" attribute is that we needa know the EXACT INDEX of our data we want to acquire
# so the better usage for acquiring data is the "loc" attribute

df.loc["TEETO", : ] # df.loc[row_name, column_name]   use " : " to mean "ALL" data
df.loc[("TEETO", "Trist"), : ]
df.loc[("TEETO", "Trist"), ("Kills", "Deaths")] #more than one certain data, use '()' to put em together
df.loc["TEETO":"Urgot", "Deaths" : "Assists"] # what to (:) what
df.loc[ : "Urgot", "Deaths" : ]  #start to(:) what, something to(:) End

#the "iloc" attribute uses (row, column)
df.iloc[1, : ]
df.iloc[1][1] #.iloc is the exact same usage as .loc, but it uses the exact index

df.ix[]  # works exactly like the same as the previous two, but a combination of both, can use index and names at the same time
df.head(10) # list out the from 10 data of the data frame
df.tail(5) # list our the last 5 data of the data frame

#to change the data of the data frmae
df.ix["TEETO"]["Deaths"] = 333
df.ix["Urgot", : ] = 10 # change all of its value to 10

#SORT DATAFRAME VALUES
#var = df.sort_values(by = column_name [, ascending = Boolean])
df1 = df.sort_values(by = "Deaths", ascending = False)
# sort by index, column name
#var = df.sort_index(axis = row_column_value (0 or 1, 0 : sort by ROW_Title, 1 : sort by COL_Title) [, ascending = Boolean]) 
df2 = df.sort_index(axis = 0)

#Deleting Values in Pandas
#using .drop
# df = df.drop(column_or_row_name  [, axis = 0 or 1])
df1 = df.drop("TEETO") #deleting TEETO's KDA, all data
df2 = df.drop("Deaths", axis = 1) #dropping the kills column, all of it
df3 = df.drop(["Deaths", "Assists"], axis = 1) # droping more then one, use brackets to put em all in []
df4 = df.drop(df.index[1:3]) # droping a whole bunch of characters from where to where with their index
df5 = df.drop(df.columns[0:2], axis = 1) #dropping column data

 