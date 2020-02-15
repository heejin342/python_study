"""
판다스 ,매트플롯 패키지를 활용한 시각화하기
"""

import matplotlib.pyplot as plt
import pandas as pd

#한글 깨짐현상 해결
from matplotlib import font_manager,rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

temperature = [25.2 , 27.4, 22.9, 26.2 , 29.5 , 33.1 , 30.2, 36.1, 34.4, 29.1]
Ice_cream_sales = [236500,357500,203500,362500,446600,574200,453200,675400,463100,876500]



#사전 객체 생성
dict_data = {'기온 일일최고 온도' : temperature , '아이스크림 판매량':Ice_cream_sales}
df_ice_cream = pd.DataFrame(dict_data, columns=['기온 일일최고 온도', '아이스크림 판매량'])


#데이터 시각화
df_ice_cream.plot.bar(x= '기온 일일최고 온도' , y='아이스크림 판매량' , grid = True, title= '최고기온과 아스크림 판매량의 관')
plt.show()

                