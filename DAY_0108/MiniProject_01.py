# [아이유 콘서트 예매 시스템]
# 좌석 100개(퍼스트 20개, 비즈니스 30개, 이코노미 50개)
# 빈 리스트 생성 >> 예매 완료된 좌석의 숫자를 리스트에 추가
# 리스트 안에 좌석 숫자가 있는 경우(멤버 연산자 사용), 매진된 좌석이므로 "매진되었습니다" 출력
# 없는 경우, "예약하시겠습니까?" >> " 해당 좌석은 {좌석 등급} 좌석이므로 @@ 원입니다. 결제하시겠습니까?"
# >> "예매가 완료되었습니다" or "취소되었습니다"
# 현재 남은 좌석은 @석 입니다(len(리스트)) 사용, 남은 좌석은 [리스트]가 있습니다.

def want_Pay():     # 결제 여부를 결정하는 함수
    intchoice = int(choice_book)            # 입력받은 choice_book이 str >> 숫자 비교 위해 int형으로 변환하여 저장
    if intchoice >= 1 and intchoice <= 20:  # 입력받은 좌석 번호가 퍼스트석일 경우
        print(f'선택하신 {intchoice}번 좌석은 퍼스트석이며, 결제 금액은 300,000원 입니다.')
        real_Pay = input("결제하시겠습니까? (Yes 혹은 No로 답변해주세요)")
        if real_Pay == 'Yes':
            print("==== 결제가 완료되었습니다. 예매 정보는 카카오톡으로 발송해드립니다. 감사합니다. ====")
            bookList.append(choice_book)    # 예매가 완료되면 예매 목록에 해당 좌석 추가 >> 예매 된 좌석과 안 된 좌석을 구분 가능
        elif real_Pay == 'No':
            print("==== 결제가 취소되었습니다. 처음부터 다시 시작해주세요 ====")
        else:
            print("잘못된 입력값입니다.")
    elif intchoice >= 21 and intchoice <= 50:   # 입력 좌석이 비즈니스석일 경우
        print(f'선택하신 {intchoice}번 좌석은 비즈니스석이며, 결제 금액은 200,000원 입니다.')
        real_Pay = input("결제하시겠습니까? (Yes 혹은 No로 답변해주세요)")
        if real_Pay == 'Yes':
            print("==== 결제가 완료되었습니다. 예매 정보는 카카오톡으로 발송해드립니다. 감사합니다. ====")
            bookList.append(choice_book)    # 예매 완료시 예매 목록에 추가
        elif real_Pay == 'No':
            print("==== 결제가 취소되었습니다. 처음부터 다시 시작해주세요 ====")
        else:
            print("잘못된 입력값입니다.")
    else:                                       # 예매 목록이 이코노미석일 경우(나머지 숫자 혹은 다른 값들은 본문에서 필터됨)
        print(f'선택하신 {intchoice}번 좌석은 이코노미석이며, 결제 금액은 100,000원 입니다.')
        real_Pay = input("결제하시겠습니까? (Yes 혹은 No로 답변해주세요)")
        if real_Pay == 'Yes':
            print("==== 결제가 완료되었습니다. 예매 정보는 카카오톡으로 발송해드립니다. 감사합니다. ====")
            bookList.append(choice_book)
        elif real_Pay == 'No':
            print("==== 결제가 취소되었습니다. 처음부터 다시 시작해주세요 ====")
        else:
            print("잘못된 입력값입니다.")

def booking_system():       # 예약 여부를 결정하는 함수
    book = input('예약하시겠습니까?(Yes 혹은 No로만 대답)')
    if book == 'Yes':
        want_Pay()      # 결제 여부를 확인하는 함수로 넘어감
    elif book == 'No':
        print("취소되었습니다")
    else:               # Yes 혹은 No 값이 아닌 경우, 잘못된 값으로 판정
        print("잘못된 값을 입력하셨습니다")

def del_book(x):        # 예매되지 않은 좌석 목록인 noBook 리스트에서 예매된 좌석인 bookList 요소를 제거하기 위한 함수
    for idx in range(len(x)):   # 예매한 좌석 목록은 str 형식으로 리스트에 저장 >> int 형식인 nobook 리스트와 비교하여 제거하기 위해
        x[idx] = int(x[idx])    # bookList의 요소들을 int형으로 변경
    for idx2 in range(len(x)):
        if x[idx2] in noBook:   # 만약 noBook 리스트에 예매한 좌석이 있는 경우에만 제거해줘야 함. 그렇지 않으면 잔여 좌석 확인마다 지워짐
            noBook.remove(x[idx2])  # >> 오류 발생
    for idx3 in range(len(x)):  # 비교를 위해 int형으로 전환한 bookList 항목들을 다시 str 형식으로 원상 복구
        x[idx3] = str(x[idx3])  # 다른 부분에서는 모두 str로 작동하게 코딩해놔서 꼭 해야 함.

def cancel_Book():          # 예매 취소 기능이 있는 함수
    choice_cancel_book = input("취소하실 좌석은 몇번 좌석입니까?(숫자만 입력): ")
    if choice_cancel_book in bookList and choice_cancel_book.isdecimal(): # 입력받은 값이 숫자이며 예매 완료된 좌석 목록에 존재하는 경우
        real_Cancel = input("정말 취소하시겠습니까?(Yes 혹은 No로만 대답): ")
        if real_Cancel == 'Yes':
            bookList.remove(choice_cancel_book)         # 예매를 취소했기 때문에 예매 좌석 목록에서 제거
            noBook.append(int(choice_cancel_book))      # 예매를 취소했기 때문에 잔여 좌석 목록에 추가
            noBook.sort()                               # 잔여 좌석 목록의 가시성을 높이기 위해 오름차순으로 정렬
            print("예매가 취소되었습니다. 감사합니다.")     # >> 안하면 맨 뒤에 추가되서 복잡함.
        elif real_Cancel == 'No':
            print("즐거운 콘서트 되시길 바랍니다. 감사합니다.")
        else:
            print("잘못된 답변입니다.")
    elif choice_cancel_book not in bookList and choice_cancel_book.isdecimal(): # 취소하고 싶은 좌석이 예매 좌석 리스트에 없는 경우
        print("예약되지 않은 좌석입니다. 확인부탁드립니다.")                          # >> 예약되지 않은 좌석이라는 알림 출력
    else:
        print("잘못된 입력입니다.")

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
            if choice_book in bookList:  # 예매를 원하는 좌석이 이미 예매 완료된 좌석 목록에 있을 경우
                print("이미 예약된 좌석입니다.")  # 예매 불가 메시지 출력
            elif choice_book.isdecimal() and int(choice_book) >= 1 and int(choice_book) <= 100:
                booking_system()        # 입력값이 숫자이며, 좌석수인 100 이하의 양의 정수일 경우 예매 시스템 함수로 이동
            else:                       # 나머지는 모두 잘못된 값으로 인식
                print("잘못된 입력입니다.")
        elif choice == '2':             # 2번 메뉴를 선택할 경우, 잔여 좌석을 확인하는 기능 작동
            del_book(bookList)          # 예매 좌석을 잔여 좌석 목록에서 지우는 함수 작동
            print(f'남은 좌석은 {noBook}입니다.')   # 잔여 좌석 목록을 리스트로 표현
        elif choice == '3':         # 3번 메뉴 선택할 경우, 예매 취소 함수 작동
            cancel_Book()
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