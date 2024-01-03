# :주석(comment), 인터프린터가 해석하지 않는 코드
# 주석은 코드에 대한 설명을 작성하는 용도, 필수로 해야 함.
# 주석은 ctrl + ? 키로 주석을 설정 혹은 해제 가능
# print("Hello~")

# 시키고 싶은 일: 숫자, 글자 데이터를 화면에 출력하기
# 출력하기: print( 데이터 )
# 숫자 데이터 출력 >> 정수 int
print(2024)
print(1227)
print(33) # 한줄에 한개씩 적기

# 숫자 데이터 출력 >> 실수 float
print(2.9)
print(5.123)
print(1.) # 뒤에 0이 생략된 것 >> 실수임. print 하면 1.0 이라고 출력됨

#문자/글자/문자열 데이터 출력 >> 글자 str
# 글자는 따옴표를 이용하여 '데이터' or "데이터" 로 표기해야 함.
print('홍길동')
print("지금은 겨울")
print("Happy New Year")
print("2024.") # 해당 열은 따옴표 안에 있기 때문에 문자를 나타낸 것임.

# ''' 데이터 ''', """ 데이터 """ : 여러줄 문자열
print('''Good
         Luck
         Happy''') # 여러 줄의 문자를 출력하고자 하면 따옴표 3개를 써줘야 함(주석과 혼동 금지).
print("""
        Good
        Luck
        Happy""")