#------------------------------------------------------------------------
# range() 내장함수
# - 숫자의 범위를 생성해주는 함수
# - 반환값/결과값/리턴값이: range 타입
# - 범위에 포함되는 숫자 데이터는 원소/요소라고 함 >> 인덱싱 가능
#------------------------------------------------------------------------

# 1~20 으로 구성된 정수 데이터 생성
nums = range(20) # >> 0부터 19까지 20개를 포함함. 20은 포함되지 않음.
print(nums, type(nums))
print(nums[0], type(nums[0]))
print(nums[-1], type(nums[-1]))

print(f' nums => {len(nums)}개')

# 앞부분 5개 원소까지만 추출 >> 슬라이싱
print(f' nums[0:5] => {nums[0:5]}, {type(nums[0:5])}') # range 타입을 가짐

# range를 list로 형 변환 하기: list(데이터)
print(f'list(nums) => {list(nums)}')

# 0~100으로 구성된 정수 리스트 생성해주세요
numberList = list(range(101))
print(f'numberList => {numberList}')

#-----------------------------------------------------------
# range(시작값, 끝값, 증가 or 감소값)
# - 시작값의 기본은 0. 따라서 아무것도 안 적으면 0부터 시작함.
# - 시작값을 지정할 경우, range(1,10) >> 1부터 9까지 나옴.
# - range(1, 10, 2)일 경우, 1, 3, 5, 7, 9 가 출력됨.
#-----------------------------------------------------------

# 1~100 범위에서 3의 배수만으로 구성된 리스트 생성
threes = list(range(3,101,3))
print(threes)