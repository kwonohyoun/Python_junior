# str 데이터 타입 전용의 함수. 즉, 메서드(method) 살펴 보기
# - 메서드(method)는 특정 데이터 타입에서만 사용 가능한 함수를 의미
# - 사용방법
#   변수명.메서드명() : msg = "Good" >> mas.메서드명()
#   데이터.메서드명() : "Good".메서드명()

print("Good".upper()) # upper() 메서드: str을 대문자로 모두 바꿈
print("Good".lower()) # lower() 메서드: str을 소문자로 모두 바꿈

# str이 모두 대문자인지 검사 후 결과 반환: isupper() 메서드
print("Good".isupper())

# str이 모두 소문자인지 검사 후 결과 반환: islower() 메서드
print("Good".islower())

# str이 0~9로 구성되어 있는지(10진수인지) 검사 후 결과 반환: isdecimal() 메서드 >> - 기호 인식 못하여 False로 반환
print("Good".isdecimal(), "012".isdecimal(), "-9".isdecimal())

# str이 문자로만 구성되어 있는지 검사 후 결과 반환: isalpha() 메서드 >> 한글도 True로 나옴.
print("Good".isalpha(), "Good2024".isalpha(), "한글".isalpha())

# str이 알파벳 혹은 숫자로만 구성되어 있는지 검사 후 결과 반환: isalnum() 메서드
print("Good".isalnum(), "Good2024".isalnum(), "한글".isalnum())

# str 문자에서 특정 문자/문자열로 시작하는지 검사 후 반환: startwith()
# 시작을 ?? 로 한다고 가정.
print("??Happy New".startswith("??"))
print("??Happy New".startswith("!"))

# str 문자에서 특정 문자/문자열로 끝나는지 검사 후 반환: endswith()
print("flower.jpg".endswith("jpg"))
print("flower.png".endswith("jpg"))
print("flower.txt".endswith(("jpg", "png", "txt")))  # 끝나는 단어가 jpg, png, txt 중 하나인지 찾는 것.

# str 특정 인덱스 문자를 변경해주는 메서드: replace('바꿀 문자', '새 문자', 바꾸길 원하는 갯수) 메서드 >> indexing으로는 지원하지 않는 기능.
name = "HongGulDong"
# u를 i로 변겅하고 싶을 때
print( name.replace('u','i') ) # 갯수를 적지 않으면 모든 알파벳이 바뀜.
print( name.replace('o','*') )
print( name.replace('o','*',1) )
name = name.replace('u', 'i')