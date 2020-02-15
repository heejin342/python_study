import re   

jumin ="980526-2035215"
jumin_input = input ("주민번호 입력: ")

arr1 =jumin[:6]
arr2=jumin[7:]


#정규 표현식 패턴 생성 . 자리수가 맞는지 확인
patten = re.compile('^[0-9]{6}-[0-9]{7}')
match = re.match(patten, jumin_input);
if match:
    print('입력받은 주민번호가 정규 표현식에 적합하다' )
    sum1 =0
    weight = [2,3,4,5,6,7,0,8,9,2,3,4,5]

    for i in range(0, len(weight)):
        if jumin_input[i] == '-':
            continue
        sum1 += int(jumin_input[i]) * int(weight[i])

    tmp = 11 - (sum1 % 11)
    result =  tmp%10
   
    if result == int(jumin_input[13]):
       print("정상인 주민번호입니다")
    else:
        print("틀린 주민번호 입니다")
     
else :
    print('정규 표현식에 적합하지 않습니다')




sum = int(arr1[0]) * 2 + int(arr1[1]) *3 + int(arr1[2]) * 4 + int(arr1[3]) * 5 + +int(arr1[4]) * 6 + int(arr1[5]) * 7 +int(arr2[0]) * 8 +int(arr2[1]) * 9 +int(arr2[2]) * 2 +int(arr2[3]) * 3 +int(arr2[4]) * 4 +int(arr2[5]) * 5 
print(sum)


result1 = (11 - sum%11) %10
if result1==int(arr2[6]):
    print('정상')

