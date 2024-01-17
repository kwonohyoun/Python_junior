import func

with open('func.py', mode = 'r', encoding='utf8') as f:
    funcData = f.read()

choice_cancel_book = '' # 예매 취소할 때 쓸 전역변수
choice_book = ''        # 예매 할 때 쓸 전역변수
bookList = []           # 예매 완료된 좌석 번호를 담고 있는 리스트
noBook = list(range(1,101)) # 예매되지 않은 좌석 번호를 담고 있는 리스트

while True:
    print("<<<< 아이유 콘서트에 관심을 가져주셔서 감사합니다!! >>>>")
    print("1. 예매하기")
    print("2. 남은 좌석 확인")
    print("3. 예매 취소")
    print("4. 종 료")
    print("=========================================")

    choice = input("메뉴를 선택해주세요: ")

    if choice.isdecimal():
        if choice == '1':    # 1번 메뉴를 선택했을 경우, 예매 기능 작동
            choice_book = input('좌석번호 1~20은 퍼스트석, 21~50은 비즈니스석, 51~100은 이코노미석 입니다.\n원하시는 좌석의 번호를 입력해주세요: ')
            if choice_book in func.bookList:  # 예매를 원하는 좌석이 이미 예매 완료된 좌석 목록에 있을 경우
                print("이미 예약된 좌석입니다.")  # 예매 불가 메시지 출력
            elif choice_book.isdecimal() and int(choice_book) >= 1 and int(choice_book) <= 100:
                func.booking_system()      # 입력값이 숫자이며, 좌석수인 100 이하의 양의 정수일 경우 예매 시스템 함수로 이동
            else:                       # 나머지는 모두 잘못된 값으로 인식
                print("잘못된 입력입니다.")
        elif choice == '2':             # 2번 메뉴를 선택할 경우, 잔여 좌석을 확인하는 기능 작동
            func.del_book(func.bookList)          # 예매 좌석을 잔여 좌석 목록에서 지우는 함수 작동
            print(f'남은 좌석은 {func.noBook}입니다.')   # 잔여 좌석 목록을 리스트로 표현
        elif choice == '3':         # 3번 메뉴 선택할 경우, 예매 취소 함수 작동
            func.cancel_Book()
        elif choice == '4':         # 4번 메뉴 선택할 경우, 예매 시스템 종료 >> 퇴근시 사용
            want_Off = input("정말 종료하시겠습니까?(Yes or No로만 답변): ")
            if want_Off == 'Yes':
                print("시스템을 종료합니다.")
                break
            elif want_Off == 'No':
                print("종료가 취소되었습니다.")
            else:
                print("잘못된 값을 입력하셨습니다.")
        else:
            print("잘못된 입력입니다.")
    else:               # 1, 2, 3, 4번 외에 다른 메뉴를 선택했을 경우, 모두 잘못된 값으로 취급
        print("잘못된 입력입니다.")