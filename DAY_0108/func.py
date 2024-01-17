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