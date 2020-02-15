num = input("결제 금액을 입력하세요: ")

if num.isdigit():
    num=num[::-1]
    ret = ''
    
    for i, c in enumerate(num):
        i+=1
        if i !=len(num) and i%3 ==0:
            ret +=( c + ',')
        else:
            ret +=c
            
    ret = ret[::-1]
    print(ret + "원" )
else:
    print('입력한 내용 %s는 숫자가 아닙니더' %num)