"""
A 기업의 전년도 대비 매출 실적 비교
"""

year2017 = [9,23,55,75,89,40,70,85,100,48,78,30]
year2018 = [10,27,45,67,79,56,37,59,60,40,50,70]



compareYear = list(zip(year2017 , year2018))
print(compareYear)

print("=================================================================")


range1 = range(10)
print(list(range1))

range2 = range(10,20)
print(list(range2))


print("=================================================================")

list_data = [1,5,6,8,9,2,3,1]
even = list(filter(lambda x:(x%2 ==0),list_data))
print(even)

print("=================================================================")



names= {'Mary' :10999, 'Sam':2100, 'Aimy':9800 , 'Tom':20300}
ret1=sorted(names) #소트 함수에 딕셔너리를 인자로 주면, 키를 오름차순으로 정리한다.
print(ret1)


print("=================================================================")



#def f1(x):
#    return x[0]


#람다 함수로 처리해보자!
ret2 = sorted(names.items(), key=lambda x:x[0 ])

def f2(x):
    return x[1]

#ret2 = sorted(names.items() , key=f1)        #키를 기준으로 오름차순
ret3 = sorted(names.items() , key=f2)       # 값을 기준으로 오름차순

print(ret2)
print(ret3)

ret4 = sorted(names.items() , key=f2 , reverse = True)          #값을 기준으로 내림차순
print(ret4)

print("=================================================================")





