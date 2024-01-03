# 다양한 리스트 생성
#-------------------------------------------------------

# 실수 데이터로 구성된 리스트 생성
floatNums = [ 4., 3.1, 6.3, 5.01 ]

# str 데이터로 구성된 리스트 생성
strNums = ['44', '56', '98']

# bool 데이터로 구성된 리스트 생성
boolNums = [False, False, True, True, True]

# 다양한 데이터 타입으로 구성된 리스트 생성
nums = ['100', 98, False, 7, 12, 'Apple', True]

# 빈 리스트 생성
nums2 = []

# 리스트 안에 리스트 데이터로 구성된 리스트 생성 >> 리스트 요소는 하나의 묶음으로 인덱스 매김
nums3 = [10, 20, 30, ['A', 'B'], 200, 100]

# 리스트의 요소 출력
print(f' nums3[0] => {nums3[0]}, {type(nums3[0])}')
print(f' nums3[1] => {nums3[1]}, {type(nums3[1])}')
print(f' nums3[2] => {nums3[2]}, {type(nums3[2])}')
print(f' nums3[3] => {nums3[3]}, {type(nums3[3])}') # 리스트 안에 있는 리스트 원소의 타입은 리스트임
print(f' nums3[4] => {nums3[4]}, {type(nums3[4])}')
print(f' nums3[5] => {nums3[5]}, {type(nums3[5])}')

print(f' nums3[3][1] => {nums3[3][1]}, {type(nums3[3][1])}') # 리스트 안에 있는 리스트의 원소를 빼는 법

data = [[[1, 2, 3]]]
print(data[0])
print(data[0][0])
print(data[0][0][0])