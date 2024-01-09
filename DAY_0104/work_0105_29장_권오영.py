def add(x, y):
    return x + y, x - y
a ,b = add(10, 5) # 여러 개를 반환하면 튜플이 반환됨 >> 언패킹 원리
print(a, b)

ex = add(10, 5)
print(ex) # 튜플

# 29장 퀴즈) 1번: c
# 29장 퀴즈) 2번: d
# 29장 퀴즈) 3번: a, c, d  >> 여러 개를 결과값으로 반환할 때는 콤마로 구분, 혹은 튜플이나 리스트 활용하여 여러 개 반환
# 29장 연습문제)
def get_quotient_remainder(x,y):
    return x // y, x % y
# 29장 심사문제
def calc(x, y):
    return x+y, x-y, x*y, x/y

