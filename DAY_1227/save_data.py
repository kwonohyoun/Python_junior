'''
데이터를 메모리에 저장하는 방법
>> 파이썬 문법 : 변수명(스택에 저장) = 저장할 데이터(힙영역에 저장, 힙영역 몇번에 저장된지에 대한 주소(변수명)는 스택 영역에 저장)
>> 파이썬의 변수는 힙영역에 저장된 데이터 주소를 저장하는 변수(참조 변수, reference 변수)
>> 변수명은 스택의 주소에 이름을 붙이는 것. 변수명을 통해 스택의 주소를 알아내 힙영역의 주소를 알아내고 힙영역에서 데이터 가져오는것
>> 변수명은 영어, 숫자, 언더바 사용 가능, 대신 숫자로 시작하면 안됨, 공백(띄어쓰기) 사용하지 않고 언더바 사용하기
>> 변수명만 보고도 어떤 데이터가 저장된지 잘 알 수 있어야 함
>> 만약 같은 데이터가 다양한 변수명으로 저장된다면, 힙에 한번만 저장되고 모든 변수가 해당 데이터를 참조하는 방식으로 공유(저장)됨.
'''
# 나이를 메모리에 저장하기
# >> 나이: 정수 int >> 힙 영역
# >> 변수: age
age = 100
# 'age'=100 이라고 쓰면 안됨. 문자로 인식해버림.

# 이름을 메모리에 저장하기
# >> 이름: 문자 str >> 힙 영역
# >> 변수: name
_name = "홍길동"
name = "홍길동"
my_name = "홍길동"
# 99name = "홍길동" 이라고 쓰면 안됨. 숫자는 변수 이름으로 첫번째 자리 불가. But 뒤에 오는 건 상관 없음.

# 메모리에 저장은 됨 >> 하지만 저장된 데이터의 위치 알 수 없음 >> 다시 사용 불가
2024
"Hong"

year = 2024  # 2024 데이터가 저장된 주소를 year 이름이 붙은 메모리에 저장
print(year)

# 데이터의 주소(메모리 주소)를 확인하는 내장함수 >> id( 실제 데이터 ) or id( 변수명 )
print(id(2024))
print(id(year))

year = 2023 # year라는 변수명(스택)에 저장된 주소가 2023으로 바뀌어 버렸기 때문에 id 출력시 값이 달라짐
print(id(year))

year = '2023' # 2023이라는 문자를 저장한 것. 따라서 메모리 주소가 바뀜.
print(id(year))

# 변수가 저장하고 있는 데이터의 종류, 즉 데이터 타입을 알려주는 함수 >> type( 데이터 or 변수명 )
print(type(2024))
print(type(4.))
print(type("4."))