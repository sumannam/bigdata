# 1. 데이터 준비
import matplotlib.pyplot as plt

y1 = [350, 410, 520, 695]
y2 = [200, 250, 385, 350]
x = range(len(y1))

# 2. x축과 y축 데이터를 지정하여 라인플롯 생성
plt.bar(x, y1, width = 0.7, color = "blue")
# <BarContainer object of 4 artists>
plt.bar(x, y2, width = 0.7, color = "red", bottom = y1)
# <BarContainer object of 4 artists>

# 3. 차트 제목 설정 
plt.title('Quarterly sales')
# Text(0.5, 1.0, 'Quarterly sales')

# 4. x축 레이블 설정
plt.xlabel('Quarters')
# Text(0.5, 0, 'Quarters')

# 5. y축 레이블 설정
plt.ylabel('sales')
# Text(0, 0.5, 'sales')

# 6. 눈금 이름 리스트 생성
xLabel = ['first', 'second', 'third', 'fourth'] 

# 7. 바 차트의 x축 눈금 이름 설정
plt.xticks(x, xLabel, fontsize = 10)
# ([<matplotlib.axis.XTick object at 0x0000015DB5722B48>, 
# <matplotlib.axis.XTick object at 0x0000015DB5722B08>, 
# <matplotlib.axis.XTick object at 0x0000015DB82E2688>, 
# <matplotlib.axis.XTick object at 0x0000015DB60C5188>], 
# [Text(0, 0, 'first'), Text(0, 0, 'second'), Text(0, 0, 'third'), Text(0, 0, 'fourth')])

# 8. 범례 설정
plt.legend(['chairs', 'desks'])
# <matplotlib.legend.Legend object at 0x0000020F2BBA0908>

# 9. 바 차트 표시
plt.show()
