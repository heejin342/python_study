"""

소개팅 커플맺기 어플리케이션

"""

from random import shuffle

male = ['손흥민', '이강인' , '황희찬' , '이승후' , '백승후']
female = ['김다정' , '박서현' , '유다희', '이복경' , '장소영']



shuffle(male)
shuffle(female)


couples = zip(male, female)      #zip은 튜플로 묶는거임 -> 리턴할때는 리스트로
couple_data = list(couples)

for i,couple in enumerate(couples):
    print('1커플 탄생%d: [%s] - [%s]' %(i+1,couple[0],couple[1]))


for i1,couple1 in enumerate(couple_data):
    print('2커플 탄생%d: [%s] - [%s]' %(i1+1,couple1[0],couple1[1]))
    



"""
중요 =>  zip() 와 list() 활용
"""

x = [1,2,3]
y = [4,5,6]
z = zip(x,y)

list_data = list(z)    #튶플을 이렇게 리스트로 형변환 하지 않으면 에러가 생겨버린다.
print(list_data)



