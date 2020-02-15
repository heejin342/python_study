"""
사용자가 입려가고 싶은 만큼 파일에 쓰기
"""
count = 1;
data = []
print('파일에 내용을 저장하려면 내용을 입력하지 말고 [Enter] 를 누르세요')

while True: #무한 루프
    text= input("[%d] 파일에 저장할 내용을 입력하세요:" %count)
    if text == '':
        break;
    data.append(text + '\n')
    count+=1

f = open("mydata2.txt",'w')
f.writelines(data)
f.close()

"""
파일입출력의 마지막 예제 - 파일을 열고 자동으로 닫기
"""
with open('stockcode.txt' , 'r') as f:
    for line_num, line in enumerate(f.readlines()):
        print('%d %s' %(line_num+1,line), end='')
        
        
        
        
    


















