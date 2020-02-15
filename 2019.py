import pandas
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

def word_count(text):
    wordAll=text.split(' ')
    wordDic={} 
    for i in wordAll:
        wordCnt=wordAll.count(i);
        wordDic[i]=wordCnt
    
    print("\n당신이 입력하신 문장의 단어수는 아래와 같습니다.\n")
    
    for cnts in wordDic:
        if wordDic[cnts]:
            print(cnts," : ",wordDic[cnts])

    return


    
filename = 'Womens Clothing E-Commerce Reviews.csv'
    
data = pandas.read_csv('Womens Clothing E-Commerce Reviews.csv' , header= None)
 





#print(data[3][212])   # nan
Dress_rate=[0,0,0,0,0,0] # 1점 2점 3점 4점 5점
Inti_rate=[0,0,0,0,0,0]
Pants_rate=[0,0,0,0,0,0]
Bluses_rate=[0,0,0,0,0,0]
Knits_rate=[0,0,0,0,0,0]
Lounge_rate=[0,0,0,0,0,0]
Sweaters_rate=[0,0,0,0,0,0]
Skirts_rate=[0,0,0,0,0,0]
Fine_rate=[0,0,0,0,0,0]
Sleep_rate=[0,0,0,0,0,0]
Jacket_rate=[0,0,0,0,0,0]
Swim_rate=[0,0,0,0,0,0]
Trend_rate=[0,0,0,0,0,0]
Jeans_rate=[0,0,0,0,0,0]
Legware_rate=[0,0,0,0,0,0]
Shorts_rate=[0,0,0,0,0,0]
Layering_rate=[0,0,0,0,0,0]
Casual_rate=[0,0,0,0,0,0]
Outware_rate=[0,0,0,0,0,0]
Jackets_rate=[0,0,0,0,0,0]
Legwear_rate=[0,0,0,0,0,0]
Chemises_rate=[0,0,0,0,0,0]


Dress_age=[0,0,0,0,0,0,0,0,0,0]
Pants_age=[0,0,0,0,0,0,0,0,0,0]
Bluses_age=[0,0,0,0,0,0,0,0,0,0]
Knits_age=[0,0,0,0,0,0,0,0,0,0]


rate_idx = [0,1,2,3,4,5]

cntDr = 0
cntInti = 0
alltext = ""

for i in range(23486):

    if data[10][i] == "Dresses" :        
        Dress_rate[int(data[5][i])]+=1
        Dress_age[int(int(data[2][i])/10)] +=1
        
    elif data[10][i] == "Intimates" :        
        Inti_rate[int(data[5][i])]+=1

    elif data[10][i] == "Pants" :        
        Pants_rate[int(data[5][i])]+=1
        Pants_age[int(int(data[2][i])/10)] +=1
        
    elif data[10][i] == "Blouses" :        
        Bluses_rate[int(data[5][i])]+=1
        Bluses_age[int(int(data[2][i])/10)] +=1
 
    elif data[10][i] == "Knits" :        
        Knits_rate[int(data[5][i])]+=1
        Knits_age[int(int(data[2][i])/10)] +=1

    elif data[10][i] == "Outwear" :        
        Outware_rate[int(data[5][i])]+=1
        
    elif data[10][i] == "Lounge" :        
        Lounge_rate[int(data[5][i])]+=1
    
    elif data[10][i] == "Sweaters" :        
        Sweaters_rate[int(data[5][i])]+=1
    
    elif data[10][i] == "Skirts" :        
        Skirts_rate[int(data[5][i])]+=1

    elif data[10][i] == "Fine gauge" :        
        Fine_rate[int(data[5][i])]+=1
        
    elif data[10][i] == "Sleep" :        
        Sleep_rate[int(data[5][i])]+=1
    
    elif data[10][i] == "Jackets" :        
        Jackets_rate[int(data[5][i])]+=1
    
    elif data[10][i] == "Swim" :        
        Swim_rate[int(data[5][i])]+=1
   
    elif data[10][i] == "Trend" :        
        Trend_rate[int(data[5][i])]+=1
    
    elif data[10][i] == "Jeans" :        
        Jeans_rate[int(data[5][i])]+=1
    
    elif data[10][i] == "Legwear" :        
        Legwear_rate[int(data[5][i])]+=1

    elif data[10][i] == "Shorts" :        
        Shorts_rate[int(data[5][i])]+=1

    elif data[10][i] == "Layering" :        
        Layering_rate[int(data[5][i])]+=1
   
    elif data[10][i] == "Casual bottoms" :        
        Casual_rate[int(data[5][i])]+=1

    elif data[10][i] == "Chemises" :        
        Chemises_rate[int(data[5][i])]+=1

    if data[10][i] == "Pants" :
        if(data[5][i] == "1"):
            if 60 <= int(data[2][i]): 
                if int(data[2][i]) <=70 :             
                    alltext += str(data[4][i])

   

        
"""
#사전 객체 생성
dict_data = {'RATE' : rate_idx , 'number_of_people':Knits_rate}

df_num = pandas.DataFrame(dict_data, columns=['number_of_people'])


#데이터 시각화

df_num.plot.bar()
plt.show()

"""
w = 0.5
data_x1 = Dress_rate
data_x2 = Knits_rate
data_x3 = Bluses_rate
data_x4= Pants_rate


plt.xlim(0.5,5.5)
plt.bar([i - 0.3 for i in range(len(rate_idx))], data_x1, label= 'set 1' , color = 'b', width = 0.2)
plt.bar([i - 0.1 for i in range(len(rate_idx))], data_x2, label= 'set 2' , color = 'g' ,width = 0.2 )
plt.bar([i + 0.1 for i in range(len(rate_idx))], data_x3, label= 'set 3' , color = 'r' ,width = 0.2)
plt.bar([i +0.3  for i in range(len(rate_idx))], data_x4, label= 'set 4' , color = 'black' ,width = 0.2)


print(int(int(data[2][1])/10))


print(Knits_age)

#니트에이지를 파이차트


slices = Knits_age
hobbies = ['0~10', '10~20', '20~30', '30~40', '40~50' ,'50~60', '60~70','70~80' ,'80~90' , '90~100' ]
cols = ['c', 'm', 'r', 'b','c', 'm', 'r', 'b','b']

plt.pie(slices, labels=hobbies, colors=cols, 
 startangle=90, shadow=True, 
 explode=(0,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.01), autopct='%1.2f%%')



# plt.legend() 메소드의 loc 매개 변수 항목 참조 요망
plt.legend(loc = 4)

filename = 'pieGraph01.png'
plt.savefig( filename, dpi=400, bbox_inches='tight' )
print( filename + ' 파일이 저장되었습니다.')

print(Pants_age)
print(Pants_rate)
           
plt.show()

print(alltext)

#2, 6 을 끌어올릴수 있도록 
    
word_count(alltext)