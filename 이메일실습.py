"""

이메일 입력시 데이터 유효성 체크
이메일 유형
park5901@hanmail.net
kim1234@naver.com
spec@ora.co.kr
erin0521@partner.sk.com

=================
메타문자
[] -> 0~9 
{}
\w+ => 1개 이상의 알파벳 또는 숫자
() -> 그루핑
?: 없음, or 1개

"""

import re

email_ex = ['park5901@hanmail.net',
            'kim1234@naver.com',
            'spec@ora.co.kr',
            'erin0521@partner.sk.com',
            'asd@naver.com.sk.aaa']
 # 리스트, 마지막 이메일은 .이 세개여서 틀린 이메일 주소임

pattern = re.compile('^\w+@\w+\.\w+(\.\w+)?') #이메일 주소의 패턴

for email_value in email_ex:
    result = re.match(pattern, email_value)

    if result.group() == email_value :
        print('적합한 이메일 입니다.' + email_value)
    else:
        print('부적합한 이메일 입니다.' + email_value)
        
        