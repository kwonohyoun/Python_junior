x = 10
if x ==10:
    print("yes")
else:
    print("no")

x = 15
if x >= 10:
    print('10 이상입니다.')

    if x == 15:
        print('15입니다')

    if x == 20:
        print('20입니다')

# 13장) 퀴즈1: c
# 13장) 퀴즈2: c(: 표시 없음), j(들여쓰기 안함)
# 13장) 퀴즈3: a
# 13장) 연습문제: x > 0
# 13장) 심사문제
price = int(input("가격을 입력하세요: "))
gift = input("쿠폰 이름을 입력하세요: ")

if gift == "Cash3000":
    print(price - 3000)
else:
    print(price - 5000)