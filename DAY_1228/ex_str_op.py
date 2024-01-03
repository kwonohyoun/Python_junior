# str 데이터 타입 연산

# 산술 연산: 덧셈, 뺄셈, 곱셈, 나눗셈...
msg1 = "Good"
msg2 = "Happy"

# 덧셈 연산
print(f'msg1 + msg2 => {msg1 + msg2}')
# print(f'msg1 + 10 => {msg1 + 10}') # 덧셈은 str + str 만 가능
print(f'msg1 + 10 => {msg1 + str(10)}') # int 를 str 로 변환하면 덧셈 가능


# 뺄셈 연산: 지원하지 않는 기능, 즉 str 데이터는 서로 빼지 못함.
# print(f'msg1 - msg2 => {msg1 - msg2}')

# 곱셈 연산
# print(f'msg1 * msg2 => {msg1 * msg2}') # int * str 또는 str * int 형태로만 출력 가능
print(f'msg1 * 10 => {msg1 * 10}')
print(f'3 * msg2 => {3 * msg2}')

# 비교 연산: >, <, >=, <=, ==, !=
# - str 안에 원소/ 요소 단위로 비교됨. 즉, 코드값으로 비교
print(f' "H" > "I" => {"H" > "I"}')
print(f' "Ha" > "HA" => {"Ha" > "HA"}')
# 첫 번째 자리 H 끼리 비교 후, 같기 때문에 다음 자리의 A와 a를 비교하여 참/거짓 구분
# 즉 동일한 인덱스에 있는 요소의 코드값으로 비교함. 동일하면 다음자리로 넘어감.
print(f' "ha" > "Ha" => {"ha" > "Ha"}') # 첫 번째 자리에서 이미 비교가 끝났기 때문에 다음 인덱스를 비교하지 않고 바로 True 처리

# 논리 연산: and, or, not
# - not 문자열
# str 형식의 bool을 구할 때, 따옴표 사이에 어떤 글자 혹은 공백이라도 있으면 True가 되고, 완전히 비어있으면 False가 됨.
# 즉, 요소/원소가 0개인 경우 False, 1개 이상인 경우 True
print(bool("Happy"), bool(""))
print(not "Happy")
print(f'not "" => {not ""}')

# 멤버 연산자: 원소/요소가 있는 데이터 타입의 경우에 사용
# - 요소 in 데이터 : 요소가 데이터에 포함되어 있는 경우 True, 반대는 False
# - 요소 not in 데이터 : 요소가 데이터에 미포함되어 있는 경우 True, 반대는 False
print(f'"H" in "Happy" => {"H" in "Happy"}')
print(f'"h" in "Happy" => {"h" in "Happy"}')

print(f'"H" not in "Happy" => {"H" not in "Happy"}')
print(f'"h" not in "Happy" => {"h" not in "Happy"}')

print(f'"1" in "1357" => {"1" in "1357"}')
print(f'"2" in "1357" => {"2" in "1357"}')