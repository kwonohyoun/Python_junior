# --------------------------------------------------------------------------------------------------------
# 다양한 dict 자료형 => key:value >> 하나의 데이터 덩어리
# - key로 데이터를 찾기/읽기/삭제/변경
# - key 중복 X => 중복되는 key가 있을 경우, 마지막 데이터의 key의 값으로 저장
# --------------------------------------------------------------------------------------------------------
# 이름, 점수 저장하기
jumsuDict = {'Hong':100, 'Park':98, 'Kim':88, 'Hong':50, 'Hong':77} # Hong이 중복되기 때문에 마지막 데이터 77이 저장됨(덮어쓰기)
print(f'jumsuDict => {len(jumsuDict)}개, {jumsuDict}')

# 이름/학년를 키로 해서 점수를 저장하기========================================================================
jumsuDict = {('Hong',1):100, ('Park',3):98, ('Kim',1):88, ('Hong',4):50, ('Hong',2):77} # 튜플 전체가 key가 됨
print(f'jumsuDict => {len(jumsuDict)}개, {jumsuDict}') # key는 변경이 되면 안 되므로 튜플 형태로 만들어야 함. 데이터는 리스트 가능.
print(f'jumsuDict[("Hong",2)] => {jumsuDict[("Hong",2)]}')
print(f'jumsuDict[("Hong",1)] => {jumsuDict[("Hong",1)]}')

# 키의 데이터 타입 동일해야 하나요?? 아닙니다.
testDict = {1:'Hong', 2.0:'Kim', False:100, 'name':'HongGilDong'}
print(f'testDict => {len(testDict)}개, {testDict}')

# 빈 딕셔너리 생성
emDict = {}
print(f'emDict => {type(emDict)}, {len(emDict)}개')

# 빈 리스트, 튜플, 딕셔너리, str 전부 bool 형식으로 바꾸면 False임.