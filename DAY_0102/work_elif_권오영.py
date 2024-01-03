x= 20
if x == 10:
    print('10입니다.')
elif x ==20:
    print('20입니다')
else:
    print('10도 20도 아닙니다')
    
# 15장) 퀴즈1: d,e
# 15장) 퀴즈2: e
# 15장) 연습문제
if x >= 11 and x <=20:
    print('11~20')
elif x >= 20 and x <= 30:
    print('21~30')
else:
    print("아무것도 해당하지 않음")
# 15장) 심사문제
money = 9000
age = int(input("나이를 입력하세요: "))

if age >=7 and age <= 12:
    print(money - 650)
elif age >= 13 and age <= 18:
    print(money - 1050)
elif age >= 19:
    print(money - 1250)