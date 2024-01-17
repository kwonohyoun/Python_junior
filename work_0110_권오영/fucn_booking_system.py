def booking_system():       # 예약 여부를 결정하는 함수
    book = input('예약하시겠습니까?(Yes 혹은 No로만 대답)')
    if book == 'Yes':
        want_Pay()      # 결제 여부를 확인하는 함수로 넘어감
    elif book == 'No':
        print("취소되었습니다")
    else:               # Yes 혹은 No 값이 아닌 경우, 잘못된 값으로 판정
        print("잘못된 값을 입력하셨습니다")
