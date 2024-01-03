# --------------------------------------------------------------------------------------------
# 메서드 => 특정 데이터 타입의 전용 함수를 메서드(method)라고 부름
# - 범용의 함수와 식별하기 위해서 지정한 호칭
# - 사용법: 데이터.메서드명() or 변수명.메서드명()
# --------------------------------------------------------------------------------------------

# List 전용의 메서드 살펴보기 ===================================================================
# [1] 리스트에 데이터 추가 해주는 메서드 => append(): 맨 끝에 원소로 추가
nums = []

print(f'nums: {len(nums)}개, {nums}')

nums.append(10) # List의 마지막 인덱스 다음에 데이터를 추가함(끝에 추가함)
nums.append('one')
nums.append(True)
print(f'nums: {len(nums)}개, {nums}')

# [2] 리스트에 데이터 추가 해주는 메서드 => insert(위치인덱스, 데이터): 지정 위치에 데이터 추가
nums.insert(0,2024) # 0번 위치에 데이터 저장
print(f'nums: {len(nums)}개, {nums}')

nums.insert(-1,["ABC", "DEF"]) # -1번 위치(맨 끝)에 리스트 삽입 >> True는 뒤로 밀려나버림(여전히 -1번 인덱스를 차지함)
print(f'nums: {len(nums)}개, {nums}')

# "DEF" 데이터만 지우는 법은?
del nums[-2][-1]
print(f'nums: {len(nums)}개, {nums}')

# 리스트 안에 모든 원소 삭제해서 빈 리스트 만들어주세요
del nums[:]
print(f'nums: {len(nums)}개, {nums}')

# [3] 리스트 안에 원소/요소 정렬해주는 메서드 => sort(): 오름차순 정렬
# - 오름차순: 값이 작은 데이터 >> 값이 큰 데이터
nums.append(98)
nums.append(-2)
nums.append(4)
nums.append(0)
nums.append(0.1)

nums.sort()
print(f'nums: {len(nums)}개, {nums}')

# 내림차순: 큰 데이터 >> 작은 데이터 순으로 정렬
nums.sort(reverse=True) # 역순 매개변수 값을 True로 설정
print(f'nums: {len(nums)}개, {nums}')

# [4] 리스트 안에 원소/요소의 현재 위치를 반대로 뒤집어 주는 메서드 => reverse()
# 원소/요소 데이터 값 비교 안함. 단지 순서만 바꿔줌.
nums.reverse()
print(f'nums: {len(nums)}개, {nums}')

# [5] 리스트 안에 원소/요소를 삭제해주는 메서드 => remove(데이터)
# - 리스트에서 지정된 값의 원소 삭제
# - 없는 값/데이터 삭제 요청 시 Error 발생시킴!!
nums.remove(0) # List에서 0을 지움
print(f'nums: {len(nums)}개, {nums}')

# [6] 리스트 안에 모든 원소/요소를 삭제해주는 메서드 => clear()
nums.clear()
print(f'nums: {len(nums)}개, {nums}')

# [7] 리스트에 원소/요소를 꺼내는 메서드 => pop()
nums.append(10)
nums.append(-3)
nums.append(7)
print(f'nums: {len(nums)}개, {nums}')

# 제일 마지막 원소/요소 데이터 꺼내기 => pop()
nums.pop() # 꺼내버리기 때문에 List에서 사라짐
print(f'nums: {len(nums)}개, {nums}')

# 특정 위치에 요소/원소 데이터 꺼내기 => pop(인덱스)
nums.pop(0)
print(f'nums: {len(nums)}개, {nums}')

# [8] 리스트에서 특정 원소/요소 데이터가 몇개 존재하는지 카운팅해주는 메서드 => count(데이터)
print(nums.count('A'))
print(nums.count(-3))

# [9] 리스트를 확장시키는 메서드 => extend(여러 개의 데이터 저장한 데이터 타입)
nums.extend([11, 22, 33]) # List 원본 자체가 바뀜. 즉 데이터가 합쳐져서 원본이 바뀜.
print(f'nums: {len(nums)}개, {nums}')

nums.extend([]) # 빈 리스트를 추가 >> 아무 데이터가 추가되지 않음
print(f'nums: {len(nums)}개, {nums}')

nums.extend("새해 복 많이 받으세요") # 모든 글자와 공백이 나누어져서 각각의 요소로 들어감(str 타입 데이터)
print(f'nums: {len(nums)}개, {nums}')

nums.extend( ["새해 복 많이 받으세요"] ) # 리스트에 담겨 있기 때문에 한 덩어리로 들어감(list 타입 데이터)
print(f'nums: {len(nums)}개, {nums}')

# nums.extend(2024) # 숫자는 원소/요소 라는 개념이 없기 때문에(인덱스가 없음) 오류가 발생 >> 시퀀스 or 반복 가능한 데이터만 가능
# print(f'nums: {len(nums)}개, {nums}')
# Sequence type: 순서, 즉 index가 있는 데이터 타입(list, str, range)

# [10] 리스트를 복사해주는 메서드 => 얕은 복사: copy()
nums2 = nums.copy()

print(f'nums: {len(nums)}개, {nums}')
print(f'nums2: {len(nums2)}개, {nums2}')

# nums의 -2번 요소의 데이터를 2024로 변경
nums[-2] = 2024 # nums2 요소에는 영향 끼치지 않음. copy는 각각의 list를 생성하는 것.
print(f'nums: {len(nums)}개, {nums}')
print(f'nums2: {len(nums2)}개, {nums2}')

# nums의 -1번 요소의 0번 요소의 데이터를 77로 변경
nums.append([100, 200])
print(f'nums: {len(nums)}개, {nums}')
nums[-1][0] = 77
print(f'nums: {len(nums)}개, {nums}')
print(f'nums2: {len(nums2)}개, {nums2}')

# 리스트 안에 내부 리스트가 있는 경우를 copy 할 경우, 내부 리스트 주소는 공유함.
# 따라서 내부 리스트가 바뀔 경우, copy한 리스트는 각각의 리스트지만 내부 리스트는 함께 바뀜