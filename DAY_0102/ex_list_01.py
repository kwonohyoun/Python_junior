# -------------------------------------------------------------------------------
# List => 여러 개의 데이터를 저장하는 데이터 타입
# - 문법 => [ 데이터1, 데이터2, ..., 데이터n ]
# - 원소/요소 => 식별하기 위해서 인덱스(Index) 사용: 파이썬에서 명명
# - 인덱싱 기능/ 슬라이싱 기능 모두 사용 가능
# -------------------------------------------------------------------------------

# 1~50 범위의 7의 배수에 해당하는 정수로 구성된 리스트 생성
num = list(range(7,51,7))

# str 데이터 타입 => 인덱싱 : 요소 변경 X, But List는 요소 변경 가능
# 제일 첫번째 인덱스에 있는 원소 삭제 => del 삭제하고 싶은 데이터 or del(삭제하고 싶은 데이터)
del num[0]
del(num[0])

# del num >> 리스트 객체 주소를 저장하는 변수 삭제(List가 모두 지워짐)

# --------------------------------------------------------------------------------------------
# 리스트에 인덱싱 방식으로 원소/요소 데이터 변경 및 삭제 가능, But 추가는 불가능 >> 메서드 이용해야 함.
# --------------------------------------------------------------------------------------------
# 요소 갯수 5개 이므로 인덱스는 0~4까지 존재
num[4] = 56 # 4번째 인덱스를 56으로 변경하는 방법
