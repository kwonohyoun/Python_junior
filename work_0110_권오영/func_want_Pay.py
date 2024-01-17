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
