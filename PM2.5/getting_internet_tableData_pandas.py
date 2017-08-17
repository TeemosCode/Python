#needa install "html5lib" module first : conda install html5lib
# pandas read in data from different sources, and has different apis for em:
"""
read_cvs()
read_excel()
read_sql()    reading sqlite
read_json()
read_html()

#as their name suggests lol
"""
import pandas as pd
tables = pd.read_html("http://www.stockq.org/market/commodity.php") # returns DataFrame object list
# finding the row (<table>) data we want and need in the html
n = 1
for table in tables:
	print("The '" + str(n) + "th' table")
	print(table.head())
	print()
	n += 1

"""
has tons of ouputs, but the '8th' table is what we need:
the ouput as followed:

The '8th' table
                  0        1        2       3      4
0  商品價格 (Commodity)      NaN      NaN     NaN    NaN
1                商品       買價       漲跌      比例     台北
2                黃金  1286.73     3.62   0.28%  03:00
3                 銀  17.0415  -0.0765  -0.45%  03:00
4                白金   975.34    -3.97  -0.41%  03:00



"""

#now all we needa do is to set up our data, data curation and manipulation (we dont need the front 2 rows of this table)
table = tables[7] # grab the 8th table
table = table.drop(table.index[[1,0]]) # dropping 1 and 0 index, more than one so put em in brackets []
table.columns = ["Commodities", "Price", "Growth", "Percentage", "Taipei_Time"]
table.index = range(len(table.index))
print(table)
#the output
'''
 Commodities    Price   Growth Percentage Taipei_Time
0           黃金  1288.41      5.3      0.41%       03:54
1            銀  17.0376  -0.0804     -0.47%       03:55
2           白金      974    -5.31     -0.54%       03:55
3            鈀   921.43     6.13      0.67%       03:55
4            銅   2.9262    -0.02     -0.64%       01:59
5            鎳   4.8270    -0.03     -0.65%       01:59
6            鋁   0.9443    -0.01     -0.68%       01:59
7            鋅   1.3860    -0.03     -1.83%       01:59
8            鉛   1.0878    -0.05     -4.14%       01:59
9            鈾    20.50     0.35      1.74%       08/07
10        黃金期貨   1294.4     11.5      0.90%       03:43
11         銀期貨    17.04      0.1      0.59%       03:43
12         銅期貨    293.2    -2.15     -0.73%       03:43
13        天然氣期    2.917    0.027      0.93%       03:43
14       布蘭特油期    50.92     0.65      1.29%       03:43
15       紐約輕原油    47.03     0.25      0.53%       03:43
16        燃油期貨   158.06     0.62      0.39%       03:43
17        玉米期貨   364.25    -2.25     -0.61%       02:19
18        小麥期貨   440.75    -6.25     -1.40%       02:19
19        可可豆期     1869       30      1.63%       01:29
20        黃豆期貨      933     7.75      0.84%       02:19
21       黃豆油期貨    33.55     0.37      1.12%       02:19
22        咖啡C期   132.05    -2.45     -1.82%       01:29
23        十一號糖    13.29     0.35      2.70%       12:59
24        二號棉期    66.91     0.09      0.13%       02:19
25        活牛期貨  106.225     -2.1     -1.94%       02:04
26        瘦豬期貨   66.925    -1.85     -2.69%       02:04

'''