def print_nums(x, y, z):
    print(x)
    print(y)
    print(z)

x = [ 10, 20 ,30]
print_nums(*x) # *모양을 통해 리스트나 튜플의 포장을 풀어 순서대로 넣는다고 생각하면 됨.

def print_numbers(*args):
    for arg in args:
        print(arg)
y = [10]
z = [15, 13, 18, 20, 41]
print_numbers(*y)
print_numbers(*z)

def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)
dict = {'name':'kwon', 'age':26, 'address':'daegu'}
personal_info(name='Kwon', age=26, address='daegu')
personal_info(**dict) # 딕셔너리를 언패킹 할 떄 *을 한번만 사용하면 키를, 두 번(**) 사용하면 두 번 언패킹하여 값을 사용함.

print('-----------------------------------------------')
def personal_info(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ':', arg, sep='')

personal_info(**dict)
personal_info(name='권오영')

def personal_info2(name, age, address='비공개'): # 매개변수 = '기본값' 형태를 통해 인수에 기본값을 줄 수 있음.
    print('이름: ', name)                        # 초기값이 지정된 매개변수는 맨 마지막으로 적어야 함.
    print('나이: ', age)
    print('주소: ', address)

personal_info2('권오영', 26)

# 30장 퀴즈) 1번: d
# 30장 퀴즈) 2번: b, c
# 30장 퀴즈) 3번: a, c
# 30장 연습문제)
def get_max_score(*scores):
    return max(socores)

# 30장 심사문제)
def get_min_max_score(*subject):
    return min(subject), max(subject)

def get_average(**points):
    value = 0
    for point in points:
        value = value + point
    return value/len(points)

