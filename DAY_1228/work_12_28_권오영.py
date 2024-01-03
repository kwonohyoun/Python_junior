# 1-1번
mail = "kim1234@naver.com"
print(mail[:7])

# 1-2번
ad = "http://www.naver.com"
print(ad[7:])

# 1-3번
Eng = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRr"
print(f'대문자는 {Eng[::2]}')
print(f'소문자는 {Eng[1::2]}')

# 1-4번
Eng2 = "ABC1DEF2GHI3JKL4MNO5PQR6STU7VWX8YZ"
print(Eng2[3::4])

# 1-5번
num = "881120-1068234"
print(num[:6])
print(num[7:])

# 2번
number = int(input("정수 입력: "))
x = hex(number)
o = oct(number)
b = bin(number)
print(f'10진수 : {number}')
print(f'16진수 : {x}')
print(f'8진수 : {o}')
print(f'2진수 : {b}')

# 3번
word1 = input("첫 번째 단어를 입력하세요: ")
word2 = input("두 번째 단어를 입력하세요: ")
word3 = input("세 번째 단어를 입력하세요: ")
print(f'코드 값이 가장 큰 단어 : {max(word1, word2, word3)}')
print(f'코드 값이 작은 단어 : {min(word1, word2, word3)}')
# max에 문자열이 들어가면 문자열의 코드값을 비교하여 큰 값을 출력함. 첫 번째 글자가 같다면, 다음 글자를 비교해 나가며 결과 출력함.

# 4번
msg = "내일은 불타는 금요일입니다"
word4 = input("단어 입력: ")
print(f'\'{word4}\' 단어 메시지 존재 여부: {word4 in msg}')

# 5번
word5 = input("단어 입력: ")
print(f'\'{word5}\' 코드값 : {bin(ord(word5[0]))} {bin(ord(word5[1]))[2:]} {bin(ord(word5[2]))[2:]}')