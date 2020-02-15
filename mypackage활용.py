"""
패키지 만드는 순서 -->
1|mypackage라는 이름의 디렉토리 생성
2|mylib모듈을 1번 패키지에 붙여넣는다 
3|mypackage 디렉토리에 __init__.py 파일에 version=1.0<- 이 문장만 집어넣고 저장하기


mypackage활용방법
"""
import mypackage.mylib2 


ret1 = mypackage.mylib2.add_txt('패키지' , '테스트')
ret2 = mypackage.mylib2.reverse(100,200,300)

print(ret1)
print(ret2)






