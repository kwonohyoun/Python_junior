lux1 = dict(health = 490, mana = 334, melee = 550, armor = 18.72)
print(lux1['health'])

lux1['health'] = 2000
print(lux1['health'])

# 12장) 퀴즈1: b
# 12장) 퀴즈2: e
# 12장) 퀴즈3: c
# 12장) 퀴즈4: d
# 12장) 연습문제: camille['health'] / camille['movement_speed']
# 12장) 심사문제
word1 = input("능력치 이름과 수치를 입력하세요: ")
word2 = input("능력치 이름과 수치를 입력하세요: ")
word3 = word1.split()
word4 = word2.split()
word5 = {word3[0]:word4[0], word3[1]:word4[1], word3[2]:word4[2], word3[3]:word4[3]}
print(word5)