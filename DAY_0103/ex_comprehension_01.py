# --------------------------------------------------------------------------------------------
# 컨프리헨션(comprehension)
# - List Comprehension, Dict Comprehension, Set Comprehension
# --------------------------------------------------------------------------------------------

# [실습1] aList의 원소의 값을 제곱한 값을 원소로 가지는 bList 생성하세요.
aList = [1, 2, 3, 4, 5]

bList = []
for a in aList:
    bList.append(a**2)
print(f'aList => {aList}')
print(f'bList => {bList}')

cList = [ a**2 for a in aList]
print(f'cList => {cList}')

# [실습2] aList의 원소의 값중에서 짝수인 데이터만 제곱한 값을 원소로 가지는 bList 생성하세요.
bList2 = []
for a in aList:
    if not a % 2:
        bList2.append(a**2)

print(f'bList2 => {bList2}')

# 컴프리핸션 방식
cList2 = [ a**2 for a in aList if not a%2]  # if문이 True인 경우만 a**2 실행
print(f'cList2 => {cList2}')

# [실습3] aList의 원소 값중에서 짝수인 데이터는 제곱, 홀수인 데이터는 그대로 저장한 bList 생성하세요.
bList3 = []
for a in aList:
    if not a%2:
        bList3.append(a**2)
    else:
        bList3.append(a)
print(f'bList3 => {bList3}')

# 컴프리핸션 방식
cList3 = [ a**2 if not a%2 else a for a in aList]
print(f'cList3 => {cList3}')

cList4 = { a:a**2 if not a%2 else a for a in aList}
print(f'cList4 => {cList4}') # 딕셔너리를 손쉽게 생성
