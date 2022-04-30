import numpy as np
 
lst = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
a = np.array(lst)
 
# 정수 인덱싱
s = a[[0, 2], [1, 3]]
 
print(s)
# 출력
# [2 12]