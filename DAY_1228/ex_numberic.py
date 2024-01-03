'''
논리 연산자 >> and, or, not
- 결과: True or False
- 동장방식
    * and: A and B >> A와 B 모두 True 일 때만 True
    * or: A or B >> A,B 중 하나 이상 True가 되면 True
    * not: not A >> 현재 A의 상태를 반대로 나타냄 >> not True 이면 False로, not False 이면 True >> 토클(toggle)이라 부름
'''
no1 = 10
no2 = 3 # no1, no2 = 10, 3 도 가능

# and 연산자
# 숫자 no1은 no2보다 크고, 그리고 100보다 큰 수
print(no1>no2, no1>100)
print(no1>no2 and no1>100)
print(no1>no2 and no1>100 and no1>0)

# or 연산자
# 1개 이상만 True가 되면 True로 결정
print(no1>no2, no1>100)
print(no1>no2 or no1>100)
print(no1>no2 or no1>100 or no1>0)

# not 연산자
# 현재 값을 반대로, 즉 True를 False로, False를 True로 나타냄
# False: 0, True: 1 or 0이 아닌 숫자
# not 데이터, 변수명, 수식
print( not False, not True )
print( not 0, not 1 )
print( not 2, not -3, not 0.0) # 0.0을 넣으면 자동 형변환을 통해 0으로 인식

'''
객체 비교 연산자: is, is not
- 결과: True, False
- 동작방식
    * is: A is B >> A, B가 동일한 데이터 타입의 객체 여부
    * is not: A is not B >> A, B가 서로 다른 데이터 타입의 객체 여부
'''

print(f'10 is 10 => {10 is 10}, 10 == 10 => {10 == 10}')
print(f'10 is 10.0 => {10 is 10.0}, 10 == 10.0 => {10 == 10.0}')
print(10 is 10)

# [실습] 2개 숫자 데이터 입력 받은 후 2개의 값을 산술 연산 결과를 출력해주세요.
# [출력 예시] 10 + 4 = 14
n1 = int(input("첫 번째 숫자를 입력하세요: "))
n2 = int(input("두 번째 숫자를 입력하세요: "))
print(f'{n1} + {n2} = {n1+n2}\n{n1} - {n2} = {n1-n2}\n{n1} * {n2} = {n1*n2}\n{n1} / {n2} = {n1/n2}\n{n1} // {n2} = {n1//n2}\n{n1} % {n2} = {n1%n2}\n{n1} ** {n2} = {n1**n2}')

# [실습2] [실습1]에서 입력 받은 숫자 데이터를 활용하여 비교 연산 결과를 출력하세요.
# [출력 예시] 10 > 4  => True
#           10 == 4  => False
print(f'{n1} > {n2} => {n1>n2}')
print(f'{n1} < {n2} => {n1<n2}')
print(f'{n1} >= {n2} => {n1>=n2}')
print(f'{n1} <= {n2} => {n1<=n2}')
print(f'{n1} == {n2} => {n1==n2}')
print(f'{n1} != {n2} => {n1!=n2}')

# [실습3] [실습1]에서 입력 받은 숫자 데이터를 활용하여 최대값과 최소값을 추가로 입력 받은 후 논리연산 결과 출력하세요.
# [출력 예시] 10 > 4 and 10 > 최대값       => True
#            10 > 4 and 10 > 최소값       => True
#            not 10                      => False
max = int(input("최대값을 입력하세요: "))
min = int(input("최소값을 입력하세요: "))
print(f'{n1} > {n2} and {n1} > {max}   => {n1 > n2 and n1 > max} ')
print(f'{n1} > {n2} and {n1} > {min}   => {n1 > n2 and n1 > min} ')
print(f'not {n1}       => {not n1}')