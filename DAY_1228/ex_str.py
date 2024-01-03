# 문자/ 문자열 데이터 살펴보기 >> str 데이터 타입
# - 문법: '데이터' or "데이터" or '''데이터 여러줄''' or """데이터 여러줄"""
msg = "Happy New Year 2024!"
print(msg)

# 문자/ 글자 안에서 일부분만 추출해서 다루기(문자에 번호를 매김 >> Indexing(인덱싱))
# - 왼쪽에서 오른쪽으로 갈 때: 0부터 1, 2, ...
# - 오른쪽에서 왼쪽으로 갈 때: -1부터 -2, ...
# - 원소/ 요소 추출 문법: 변수명[인덱스]
print(f'0번 원소 => {msg[0]}')
print(f'1번 원소 => {msg[1]}')
print(f'19번 원소 => {msg[19]}')

# index out of range : 인덱스 범위 벗어나면 오류 발생
# print(f'20번 원소 => {msg[20]}') >> 19번까지 있지만 20을 적어버리면 오류가 생김. exit code 1 이 뜨면 무엇인가 잘못됐다는 뜻임.

# Happy만 화면에 출력하기
print(msg[0], msg[1], msg[2], msg[3], msg[4], sep='')
# 2024!만 화면에 출력하기
print(msg[-5], msg[-4], msg[-3], msg[-2], msg[-1], sep='')

# 슬라이싱(Slicing): 변수명[ 시작 인덱스 : 끝 인덱스 + 1 : 간격 ]
# 조건: 연속된 숫자의 인덱스 or 규칙이 있는 인덱스만 사용 가능
# 간격은 자동으로 1로 설정됨(대부분의 인덱스는 연속되어 있기 때문)
# 일일이 하나씩 적을 필요 없음. 대신 끝은 해당 숫자를 표현하지 않음.
# ex) 변수명[6:9] >> 6, 7, 8 을 포함하고 9는 포함하지 않음.
print(f'msg[0:4] => {msg[0:4]}')
print(f'msg[0:5] => {msg[0:5]}')

# 2024!만 화면에 출력하기 => 슬라이싱으로 출력
print(f'msg[15:20] => {msg[15:20]}')
print(f'msg[-5:20] => {msg[-5:20]}') # 마지막에 0 넣으면 안되므로 그냥 20을 넣어주면 됨.

# 첫 번째 자리부터 시작하는 경우, 시작 인덱스를 생략 가능
print(f'msg[0:5] => {msg[0:5]} , msg[:5] => {msg[:5]}')

# 마지막까지 모두 쓰는 경우, 마지막 인덱스 생략 가능
print(f'msg[-5:20] => {msg[-5:20]}, msg[-5:] => {msg[-5:]}')

# 처음부터 끝까지 모두 출력하는 경우: 시작과 끝 모두 생략해버리면 됨.
print(f'msg[:] => {msg[:]}')

# 연속적이지 않지만, 규칙이 있는 경우의 슬라이싱
# - 변수명[ 시작 인덱스 : 끝 인덱스 + 1 : 간격/규칙 ]
msg = "123456789"
# msg 안에서 2, 4, 6, 8 요소만 출력 >> 연속은 아니지만 인덱스 간격이 2씩 증가하고 있음.
print(msg[1], msg[3], msg[5], msg[7], sep='')
print(msg[1:8:2])  # 처음 시작은 1이고, 끝은 7 + 1 인 8, 인덱스 간격은 2칸씩
# msg 안에서 3의 배수만 출력
print(msg[2::3])