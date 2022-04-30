import pandas as pd
import matplotlib.pyplot as plt

column_name = ['Python', 'BigData', 'AI']

score = pd.DataFrame([[84, 85, 92]
                     , [75, 94, 82]
                     , [77, 64, 98]]
                     , index = ['1번', '2번', '3번']
                     , columns = column_name[0:3])
print("--- 학생별 과목 성적 ---")
print(score, "\n")

df = pd.DataFrame(score)
mean_df = df.mean(axis=1)
print("--- 학생별 과목 평균 ---")
print(mean_df, "\n")

df = pd.DataFrame(score)
mean_df = df.mean(axis=0)
print("--- 과목별 평균 ---")
print(mean_df, "\n")


plt.plot(['Python', 'BigData', 'AI'], mean_df)
plt.show()

# Ref
# https://www.delftstack.com/ko/howto/python-pandas/how-to-get-average-of-a-column-of-a-pandas-dataframe/