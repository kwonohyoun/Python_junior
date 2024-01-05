# ----------------------------------------------------------------------------------------
# 반복문과 내장함수 => map(), zip() => 이용할 때 원하는 타입으로 형변환하고 쓰기
# ----------------------------------------------------------------------------------------
xList = ['1', '3', '5', '7']

# xList 안의 모든 원소를 정수 int로 변환 후 저장해주세요.
xList[0] = int(xList[0])
xList[1] = int(xList[1])
xList[2] = int(xList[2])
xList[3] = int(xList[3])
print(f'xList => {xList}')

for idx in range(len(xList)):
    xList[idx] = int(xList[idx])
print(f'xList => {xList}')

# ----------------------------------------------------------------------------------------
# 시퀀스 또는 반복이 가능한 객체의 요소/원소에 적용 후 값을 다시 저장해야 하는 경우
# 자주 사용되는 기능으로 내장함수로 제공 => map()
# - 문법: map(함수명, 시퀀스 또는 반복이 가능한 객체)
# ---------------------------------------------------------------------------------------
# int 요소인 xList를 str요소로 변환
result = list(map(str, xList))
print(f'result => {result}')
print(f'xList => {xList}')


# ----------------------------------------------------------------------------------------
# list 데이터를 dict 데이터로 생성
# ----------------------------------------------------------------------------------------
x = ['std01', 'std02', 'std03']
y = 90, 100, 99

# 방법 (1) -- 기호/부호 {}
xyDict1 = {}
xyDict1['std01'] = 90
xyDict1['std02'] = 100
xyDict1['std03'] = 99

for idx in range(len(x)):
    xyDict1[x[idx]] = y[idx]

# 방법 (2) -- dict() 생성자 함수
xyDict2 = dict()
xyDict2['std01'] = 90
xyDict2['std02'] = 100
xyDict2['std03'] = 99

for idx in range(len(x)):
    xyDict2[x[idx]] = y[idx]

# 방법 (3) -- dict( [ (키1,값1), (키2,값2), ...., (키n,값n) ] ) 생성자 함수
xy = []
for idx in range(len(x)):
    xy.append(( x[idx], y[idx]))

print(xy)

xyDict3 = dict(xy)
print(xyDict3)

# 방법 (4) -- dict( [ (키1,값1), (키2,값2), ...., (키n,값n) ] ) 생성자 함수
# By 내장함수 zip()
xyDict4 = dict(zip(x,y))
print(xyDict4)