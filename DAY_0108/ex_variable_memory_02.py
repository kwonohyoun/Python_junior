# ----------------------------------------------------------------------------------------------
# 참조형 변수 => 데이터의 주소 저장
# ----------------------------------------------------------------------------------------------
# 저장된 변수와 데이터의 관계======================================================================

num = 12
print(f'num => {id(num)}, {type(num)}')

num = 3
print(f'num => {id(num)}, {type(num)}')

num = 'Good'
print(f'num => {id(num)}, {type(num)}')

num1 = []
print(f'num1 => {id(num1)}, {type(num1)}')

num2 = [11, 22.1]
print(f'num2 => {id(num2)}, {type(num2)}')
print(f'num2[0] => {id(num2[0])}, {type(num2[0])}')
print(f'num2[1] => {id(num2[1])}, {type(num2[1])}')

print("============================ 값 변경 =============================")

# 리스트의 원소를 변경하는 경우
num2[0] = 100
print(f'num2 => {id(num2)}, {type(num2)}')
print(f'num2[0] => {id(num2[0])}, {type(num2[0])}')

# 리스트를 다른 리스트로 변경
num1 = num2 # 리스트 한개를 2개 변수 참조 >> 같이 바뀌어 버림
print(f'num1 => {id(num1)}, {num1}')
print(f'num2 => {id(num2)}, {num2}')

num1[0] = 77
print(f'num1 => {id(num1)}, {num1}')
print(f'num2 => {id(num2)}, {num2}')