import pandas as pd
 
data_dic = {
	'year': [2018, 2019, 2020],
	'sales': [350, 480, 1099]
}
print(data_dic)
# {'year': [2018, 2019, 2020], 'sales': [350, 380, 1099]}

df1 = pd.DataFrame(data_dic)
print(df1)
#     year     sales
# 0   2018     350
# 1   2019     380
# 2   2020    1099
