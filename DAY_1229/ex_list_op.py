# -------------------------------------------------------------
# List 자료형의 연산 살펴보기
# - 산술연산
# - 비교연산
# - 멤버연산자
# -------------------------------------------------------------

# 1~50 범위의 2의 배수로 구성된 리스트 생성
two = list(range(2,51,2))

# 산술연산 => 덧셈(+), 곱셈(*)
print(two + ['A', 'B'])

datas = two + ['A', 'B']
print(datas)

# list + str >> list + list(str) >> str 을 list로 캐스팅 해줘야 함 >> A, B, C 가 원소 단위로 따로 들어가짐
print(two + list("ABC"))

# list + str >> str(list) + str >> list가 전부 통째로 하나의 str로 됨. 즉 인덱스 0번이 대괄효([)가 나옴.
print( str(two) + "ABC")
aa= str(two)
print(aa[0])

# list * int => int만큼 원소를 반복해서 하나의 list로 만듦 >> 즉, list가 int 만큼 반복됨.
print( two * 3 )

# 멤버 연산 >> in / not in
# 결과값: True / False
print( "C" in datas )
print( 1 in datas )