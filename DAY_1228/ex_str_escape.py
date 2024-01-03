# str 데이터에서 특별한 의미를 가지는 문자를 escape 문자라고 함.
# - 형태: \알파벳1개 또는 \문자1개
# - 대표적인 예
#   \n: 줄바꿈         \t: 탭간격
#   \': '인용부호       \": "인용부호
#   \u: 유니코드        \\: 파일이나 웹 주소 경로

# 인용부호 살펴보기
print('Happy New \'Year\' 2024~!') # \을 사용함으로써 문자열을 나타내는 따옴표가 아닌, 문장을 강조할 때 쓰는 따옴표로 사용됨
print('Happy New \"Year\" 2024~!')

# 파일 경로
print("C:\\Users\KDP-48\\test.py") # \U, \t 로 인식하는 것을 막기 위해 \\을 사용 >> 경로를 표현 가능
# 파일 또는 데이터 경로일 경우, 이스케이프 문자를 비활성화 설정 가능
# r'경로' 또는 R'경로'
print(r'C:\Users\KDP-48\test.py')