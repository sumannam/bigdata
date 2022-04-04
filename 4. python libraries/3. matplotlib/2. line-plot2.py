import matplotlib.pyplot as plt

# 1. 데이터 준비
x = [2016, 2017, 2018, 2019, 2020]
y = [350, 410, 520, 695, 543]

# 2. x축과 y축 데이터를 지정하여 라인플롯 생성
plt.plot(x, y)
# [<matplotlib.lines.Line2D object at 0x0000015DB82D58C8>]

# 3. 차트 제목 설정 
plt.title('Annual sales') 
# Text(0.5, 1.0, 'Annual sales')

# 4. x축 레이블 설정
plt.xlabel('years') 
# Text(0.5, 0, 'years') 

# 5. y축 레이블 설정
plt.ylabel('sales')
# Text(0, 0.5, 'sales')

# 6. 라인플롯 표시
plt.show()