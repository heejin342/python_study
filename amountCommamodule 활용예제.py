"""
amountComma 모듈 활용하기 예제
"""

import amountComma as ac

num = input("결제 금액을 입력하세요")

if num.isdigit():
    amount = ac.number_Comma(num)
    print('결제금액:' , amount)
else:
    print('입력한 내용 %s 는 숫자가 아닙니다' %num)