def countBirth():
    ret=[]
    filename = 'names/yob2015.txt' #이거중요 !
    with open(filename , 'r') as f: #이거중요 !
        data =f.readlines()
        for d in data:
            if d[-1] == '\n' :        #-1은 젤 마지막거임
                d = d[:-1]             #-1 미만 ==-2 까지만 가져오겠다
                birth = d.split(',')[2]
                ret.append(birth)
    return ret

result = countBirth()
with open('new.csv' , 'w') as f:

     for birth in result:
        data='%s\n' %(birth)
        print(data , end="")
    
        f.write(data)
