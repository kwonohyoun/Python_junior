# 객체 비교 연산자 살펴보기
# >> 객체(object)는 메모리 힙 영역에 존재하는 데이터
# >> 데이터의 설명서/ 명세서에 해당하는 클래스(class)를 기반으로 객체 생성
# >> 파이썬의 모든 데이터는 객체(object)
# >> 같은 객체인지, 즉 같은 힙 영역을 참조하고 있는지 판별하는 것.

# print ( 10 is 10 )

no1 = 10
no2 = 10
no3 = 20
print( no1 is no2 )
print( no1 is no3 )