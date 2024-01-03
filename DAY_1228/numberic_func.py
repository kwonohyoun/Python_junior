# 숫자 데이터 관련 내장 함수들 살펴보기
# 내장함수: built in 함수, 즉 기본으로 제공되는 함수

# 절대값 반환하는 내장함수: abs(숫자 데이터)
num = 3
print(f'{num}의 절대값 : {abs(num)}')

num = -3
print(f'{num}의 절대값 : {abs(num)}')

# 실수값에서 소수점 이하 자리수 처리해주는 내장함수: round(실수데이터,소수점 이하 자리숫자) >> 소수점 자리 안 적으면 소수점 없음.
num = 1.23456789
print(f'{num}')
print(f'{num} => {round(num, 1)}') # 소수점 이하 자리를 1자리로 출력, 지정된 자리수 바로 뒤 숫자를 반올림 해서 출력해줌.
print(f'{num} => {round(num, 3)}') # 소수점을 버려도 반올림해서 1의 자리에 올리거나 버림.

# 가장 큰 수/ 가장 작은 수 찾아주는 내장함수: max()/ min() >> 최소 2개 이상의 데이터를 넣어줘야 함.
print( f' max(1, 2, 3) => {max(1, 2, 3)}')
print( f' max(9, 0, -3) => {max(9, 0, -3)}')

print( f' min(1, 2, 3) => {min(1, 2, 3)}')
print( f' min(9, 0, -3) => {min(9, 0, -3)}')

# 거듭제곱 계산해주는 내장함수 => pow()
print( f'pow(2, 3) => {pow(2, 3)}' )
print( f'pow(2, 8) => {pow(2, 8)}' )

# 숫자 표현 방식으로 변환 내장함수
# - 16진수로 변환 내장함수: hex(정수) >> 0x숫자 >> str 유형
# - 8진수로 변환 내장함수: oct(정수) >> 0o숫자 >> str 유형
# - 2진수로 변환 내장함수: bin(정수) >> 0b숫자 >> str 유형
num = 72
numHex = hex(num)
numOct = oct(num)
numBin = bin(num)

print(f'{num}의 16진수는 {numHex}, 8진수는 {numOct}, 2진수는 {numBin}')