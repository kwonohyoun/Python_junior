# 리스트(List) 데이터 타입
# - 여러 종류의, 여러 개의 데이터를 저장하는 타입
# - 문법: [ 데이터1, 데이터2, ...., 데이터n ]
# - 특징: 데이터 하나 하나를 요소/원소 라고 함
#        하나 하나의 요소/원소를 식별하기 위해서 인뎅싱(Indexing) 사용
# - 순서가 있는 데이터 타입: 시퀀스 데이터 타입
#----------------------------------------------------------------

# 리스트 데이터 생성
# 숫자 10개를 메모리에 저장
no1 = 10
no2 = 30
no3 = 100
no4 = 52
no5 = 100
no6 = 98
no7 = 18
no8 = 78
no9 = 10
no10 = 32

no = [ 10, 30, 100, 52, 100, 98, 18, 78, 10, 32]
print(f'id(no) => {id(no)}')
print(f'id(no[0]) => {id(no[0])}')
print(f'id(no[1]) => {id(no[1])}')

# 리스트에 원소/요소 한 개씩 접근하는 방법: 변수명[인덱스]
# 왼쪽에서 오른쪽으로 가는 인덱스: 0~
# 오른쪽에서 왼쪽으로 가는 인덱스: -1~
# 슬라이싱 가능

# [실습] 마지막 3기의 점수만 출력해주세요.
print(no[-3:])
# 짝수번째 요소만 출력해주세요
print(no[::2])
# 홀수번째 인덱스 출력
print(no[1::2])