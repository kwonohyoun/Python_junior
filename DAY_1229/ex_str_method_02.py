# str 데이터에서 특정 문자의 인덱스를 반환하는 메서드: 변수명.index('찾고자 하는 문자')
# 왼쪽에서 오른쪽으로 검사하며, 제일 먼저 발견되는 문자의 인덱스를 반환
# 존재하지 않는 문자의 str 인덱스 찾을려고 하면 Error 발생

data = "Merry Christmas"
print(data.index('C')) # 결과값 6을 출력
print(data.index('r')) # 결과값 2를 출력

first_r = data.index('r') # 제일 첫번째 발견되는 r의 인덱스를 변수에 저장
second_r = data.index('r', first_r + 1) # 첫번째 r 인덱스 이후 원소부터 하나씩 검사해서 r 찾아야 함.

print(data.index('r',4)) # 4번째 인덱스부터 찾기 시작해서 결과값 8를 출력
print(data.index('r',3)) # 3번째 인덱스부터 찾기 시작해서 결과값 3를 출력
print(data.index('r',data.index('r')+1)) # 첫 번째 r 다음에 오는 r을 찾는 방법으로, 첫 r의 인덱스에 1을 더한 곳 부터 시작.
print(data.index('r', first_r + 1)) # 첫 번째 r이 오는 곳을 변수로 설정하여 표현


# !의 인덱스를 찾기
# print(data.index('!')) # 없는 인덱스는 오류가 뜸. Not found.

# str 데이터에서 특정 문자의 인덱스를 반환하는 메서드: 변수명.find('찾고자 하는 문자')
# 왼쪽에서 오른쪽으로 검사하며, 제일 먼저 발견되는 문자의 인덱스를 반환
# 존재하지 않는 문자의 str 인덱스 찾을려고 하면 -1 반환 >> index()와의 유일한 차이점
print(data.find('!')) # !가 없기 때문에 -1을 반환함.

# str 데이터에서 문자열 분리해주는 메서드: split() 메서드
# - 기본값: 스페이스 바, 공백 기준으로 1개의 str을 여러 개의 str 분리
# - 반환값: 여러 개의 str을 담아서 리스트(list)로 반환
data = "Happy New Year"
print(type(data.split())) # list라는 타입을 가짐
# str에서 공백을 기준으로 str 나누기
datas = data.split()
print(type(datas), datas)
# list에 저장된 원소/요소 하나씩 읽기: 변수명[인덱스]  >> str의 인덱스 사용법과 동일한 방법.
print(datas[0]) # Happy 출력
print(datas[1]) # New 출력
print(datas[2]) # Year 출력

print(data.split('-')) # data에 -이 없으므로 그냥 통째로 리스트에 담아서 줌.

jumin = '123456-1234567'
juminNo = jumin.split('-')
print(juminNo)

birth = jumin[:jumin.index('-')]
numberss = jumin[jumin.index('-')+1:]
print(birth)
print(numberss)