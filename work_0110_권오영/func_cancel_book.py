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