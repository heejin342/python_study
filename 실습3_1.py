def countBirth():
    ret=[]
    for y in range(1980,2016):
        countM=0 #누계변수는 초깃값 0으로 꼭 해주기
        countF=0;
        filename = 'names/yob%d.txt' %y #이거중요 !
        with open(filename , 'r') as f: #이거중요 !
            data =f.readlines()
            for d in data:
                if d[-1] == '\n' :        #-1은 젤 마지막거임
                    d = d[:-1]             #-1 미만 ==-2 까지만 가져오겠다
                gender = d.split(',')[1]
                birth = d.split(',')[2]
                if gender == 'F':
                    countF += int(birth)
                elif gender == 'M':
                    countM += int(birth)

        ret.append((y,countM,countF))
    return ret

result = countBirth()
with open('birth_by_gender.csv' , 'w') as f:
     print('----- -------- ------')
     print('년도   남아총수  여아총수')
     print('----- -------- ------')
     for year, birthM, birthF in result:
        data='%s, %s, %s\n' %(year,birthM,birthF)
        print(data , end="")
    
        f.write(data)