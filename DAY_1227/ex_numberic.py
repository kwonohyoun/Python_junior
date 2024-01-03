"""
숫치 데이터 살펴보기
- 정수 >> class int: 양수, 음수, 0
- 실수 >> class float: 소수점 존재
- 복소수 >> class complex
"""
# [실습] 2개 정수를 입력 받기
# input() 함수 2개 사용
# str을 int로 타입 캐스팅
number1 = input("정수를 입력하세요: ")
number2 = input("정수를 입력하세요: ")
number1 = int(number1)
number2 = int(number2)

num1 = int(input("정수를 입력하세요: "))
num2 = int(input("정수를 입력하세요: ")) # 더 짧고 편함

# 비교 연산 결과 출력
# [출력] 10>3 >> True
print(f'{num1} > {num2} => {num1>num2}')
print("%d<=%d => %s" %(num1, num2, num1<=num2))
print("%d>=%d => %s" %(num1, num2, num1>=num2))
print("%d==%d => %s" %(num1, num2, num1==num2))
print("%d!=%d => %s" %(num1, num2, num1!=num2))
