import pandas as pd
 
data1 = [10, 20, 30, 40, 50]
print(data1)
# [10, 20, 30, 40, 50]

data2 = ['1반', '2반', '3반', '4반', '5반']
print(data2)
# ['1반', '2반', '3반', '4반', '5반']

sr1 = pd.Series(data1)
print(sr1)
# 0   10
# 1   20
# 2   30
# 3   40
# 4   50
# dtype: int64

sr2 = pd.Series(data2)
print(sr2)
# 0   1반
# 1   2반
# 2   3반
# 3   4반
# 4   5반
# dtype: object

sr5 = pd.Series(data1, index = [1000, 1001, 1002, 1003, 1004])
print(sr5)
# 1000   10
# 1001   20
# 1002   30
# 1003   40
# 1004   50
# dtype: int64

sr6 = pd.Series(data1, index = data2)
print(sr6)
# 1반   10
# 2반   20
# 3반   30
# 4반   40
# 5반   50
# dtype: int64

sr7 = pd.Series(data2, index = data1)
print(sr7)
# 10   1반
# 20   2반
# 30   3반
# 40   4반
# 50   5반
# dtype: object