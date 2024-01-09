# str 데이터 타입과 관련된 내장함수
# ------------------------------

# 원소/ 요소의 갯수를 알려주는 내장함수: length의 약자 len() >> 정수는 길이를 가지지 않음. 즉 len() 함수는 문자열 형식에만 사용 가능
msg = "Christmas2023!"

print(f'len(msg) => {len(msg)}개')
#print(f'len(2024) => {len(2024)}개') # 숫자 데이터는 길이, 즉 원소/ 요소를 가지지 않음.


# 문자의 코드값을 알려주는 내장 함수: ord(문자1개) >> 정수 타입을 가짐.
print(f'ord("a") => {ord("a")}') # f의 따옴표와 다른 따옴표를 사용해야 함.

# Hello의 코드값 출력하기
code_H = ord('H')
code_e = ord('e')
code_l = ord('l')
code_o = ord('o')

print(f'Hello의 코드값 => {code_H}{code_e}{code_l}{code_l}{code_o}')
print(f'Hello의 코드값 => {bin(code_H)}{bin(code_e)}{bin(code_l)}{bin(code_l)}{bin(code_o)}')
print(f'Hello의 코드값 => {bin(code_H)[2:]}{bin(code_e)[2:]}{bin(code_l)[2:]}{bin(code_l)[2:]}{bin(code_o)[2:]}')

# 코드값에 해당하는 문자를 반환해주는 내장함수 : chr(코드값)
# 코드값 65에 해당하는 문자 반환
print(f'chr(65) => {chr(65)}')


