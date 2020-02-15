"""
파이썬 클래스 만들기 + 상속하기
"""

class MyClass:
    var ='안녕하세요'
    def sayHello(self):
        print(self.var)
        
obj = MyClass() #MyClass 인스턴스 객체 생성
print(obj.var)
obj.sayHello()


class Add:
    def add(self,n1,n2):
        return n1+n2

class calculrator(Add):
    def sub(self,n1,n2):
        return n1-n2
    


obj = calculrator()
print(obj.add(100,200))
print(obj.sub(300,100))

"""
예외처리 실습예제
"""

try:
    print("안녕하세요")
    print(param)
except:
    print('ㅇ예외가발생')
finally:
    print('무조건 실행하는 코드')