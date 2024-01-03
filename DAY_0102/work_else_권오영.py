x= 5
if x ==10:
    print('10입니다')
else:
    print('10이 아닙니다')

# 14장) 퀴즈1: c
# 14장) 퀴즈2: b(들여쓰기),d(: 없음)
# 14장) 퀴즈3: True
# 14장) 퀴즈4: b, e
# 14장) 퀴즈5: a
# 14장) 연습문제: if written_test >= 80 and coding_test == True:
# 14장) 심사문제
point = input("국어, 영어, 수학, 과학 점수를 차례대로 입력하세요: ")
point = point.split()
aver = (int(point[0]) + int(point[1]) +int(point[2]) +int(point[3])) / 4

if int(point[0]) > 100 or int(point[1]) > 100 or int(point[2]) > 100 or int(point[3]) > 100:
    print("잘못된 점수")
else:
    if aver >=80 :
        print("합격")
    else:
        print("불합격")