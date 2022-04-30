import pandas as pd

data_df = [['20201101', 'Hong', '90', '95'], ['20201102',
'Kim', '93', '94'], ['20201103', 'Lee', '87', '97']]

df3 = pd.DataFrame(data_df)
df3.columns = ['학번', '이름', '중간고사', '기말고사']

df3.to_csv(".\\score.csv", header='False')

df4 = pd.read_csv(".\\score.csv", encoding='utf-8', index_col=0, engine='python')

print(df4)