"""
결제금액을 입력받아 천단위마다 꼼마(',')를 넣어  출력하는 프로그램 작성
"""
    
num = input('결제 금액을 입력하세요: ')

num= num[::-1]

if num.isdigit():
    for x in range(1, len(num)):
        
        b= num[x*3:]
        a= num[:x*3]
       
        
        c= a+','+b
        c_reverse = ''
        for char in c:
            c_reverse = char + c_reverse
        print(c_reverse)
        print(c_reverse[0])
        if(c_reverse[0]==','):
            continue
        break
        

        
        
    """    
    for x in range(1,len(num)):

        print(a)
        print(b)
        c= a+','+b
        c_reverse = ''
        for char in c:
            c_reverse = char + c_reverse
        print(c_reverse)

"""


#print ("{:,}".format(int(num)))


