"""
1.1에서 45까지 값을 저장하는 객체를만들기
2.1에서 45까지 값을 흔들기
3.그중 6개 숫자만 추출하기
4.6개 숫자를 정렬시키기. 오름차순으로
5.그걸 출력시키기
"""

from random import shuffle
from time import sleep

gamenum = input("로또 게임횟수를 입력하세요: ")

for i in range(int(gamenum)):
   # balls = [x+1 for x in range(45)]  -> 첫번째 방법
   balls = list(range(1,46))            #list함수를 이용한것
   ret = []   #빈 리스트 객체 . 아무내용도 없음
   
   for j in range(6):
       shuffle(balls)
       number = balls.pop();
       
       ret.append(number);
       
   ret.sort()   
   print('로또번호[%d]: ' %(i+1), end=' ')
   print(ret)
   sleep(1)