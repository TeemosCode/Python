import pandas as pd
import tkinter as tk
print("getting data ....")
data = pd.read_csv("http://opendata.epa.gov.tw/ws/Data/REWIQA/?$orderby=SiteName&$skip=0&$top=1000&format=csv")
print("daata GET!")

print(data)