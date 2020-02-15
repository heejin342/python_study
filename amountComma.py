"""
모듈입니다
"""
def number_Comma(num):
    num=num[::-1]
    ret = ''
    
    for i, c in enumerate(num):
        i+=1
        if i !=len(num) and i%3 ==0:
            ret +=( c + ',')
        else:
            ret +=c
            
    ret = ret[::-1]
    result=ret + "원"
    return result
