"""
실습3 --> 교수님
년도별 출생아수 계산하기
"""

def countBirth():
    ret =[]
    for y in range(1980,2016):
        count_m = 0
        count_f = 0
        filename= 'names/yob%d.txt' %y
        with open(filename,'r') as f:
            data = f.readlines()
            for d in data:
                if d[-1] == '\n':
                    d = d[:-1]
                    tmp = d.split(',')
                    gender = tmp[1]
                    birth = tmp[2]
                    if gender == 'F':
                        count_f += int(birth)
                    else :
                        count_m += int(birth) 
        ret.append((y, count_m , count_f))
    return ret



result = countBirth()

with open('bbg.csv' , 'w') as f:
    print('-------------------------------')
    for y, bm ,fm in result:
        data = '%s, %s, %s \n' %(y,bm,fm)
        print(data)
        f.write(data)                

