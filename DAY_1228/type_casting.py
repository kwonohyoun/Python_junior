'''
타입 캐스팅(Type Casting)
- 다른 데이터 타입으로 변환하는 것
- 함수: 데이터 타입명()
    * 정수: int()
    * 실수: float()
    * 문자열: str()
    * 논리: bool()
'''
# int 데이터 타입으로 형 변환
# int( 10진수 문자 '0~9' )
## str >> int
print(type(int('200')))
#print(type(int('200Day'))) # 틀린 문장: 정수형안에 문자가 들어갈 수 없음
print(type(int('200.4')))
## float >> int: 소수점 이하 데이터 손실
print(type(int(200.4)), int(200.7))
## bool >> int
## 0, 1을 False, True로 정의함.
print(type(int(False)), int(False))
print(type(int(True)), int(True), type(True))
print(type(int('True')), int('True')) # 틀린 문장: 논리형에 따옴표 사용하면 안됨.

# float 데이터 타입으로 형 변환
## str >> float('0~9인 십진수 및 실수)
print(type(float('3.5')), float('3.5'))
print(type(float('35')), float('35'))
print(type(float('-123')), float('-123'))
## print(type(float('0x123')), float('0x123')) # 틀린 문장
## int >> float
print(type(float(45)), float(45))
print(type(float(-9)), float(-9))
## bool >> float
print(type(float(False)), float(False))
print(type(float(True)), float(True))