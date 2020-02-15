"""
인기순 상위 10개 성별 출생아수

"""

from os.path import exists

def getTopBabyName(year):
    nameM = {}
    nameF = {}
    
    filename = 'names/yob%s.txt' %year
    if not exists(filename):
        print('[%s] 파일이 존재하지 않음 !' %filename)
        return None;
    with open(filename, 'r') as f:
        data = f.readlines()
        for d in data:
            if d[-1] == '\n':
                d=d[:-1]
                tmp = d.split(',')
                name = tmp[0]
                gender = tmp[1]
                birth = tmp[2]
                
                if gender == 'M':
                    ret = nameM
                    
                else: ret= nameF
                
                if name in ret:
                    ret[name] += int(birth)
                else:
                    ret[name] = int(birth)
                    
    retM = sorted(nameM.items(),key=lambda x:x[1], reverse = True)
    retF = sorted(nameF.items(),key=lambda x:x[1], reverse = True)
    
    for i, name in enumerate(retM):
        if i > 9 :
            break
        print('Top_%d 남자아이이름: %s' %(i+1 , name))
        
    print('\n')
    
    for i, name in enumerate(retF):
        if i > 9 :
            break
        print('Top_%d 여자아이이름: %s' %(i+1 , name))


y = input('인기순 상위 10개 이름을 알고싶은 출생년도를 입력하세요: ')
getTopBabyName(y)

                    
                
                
        
        
    