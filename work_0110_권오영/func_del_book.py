def del_book(x):        # 예매되지 않은 좌석 목록인 noBook 리스트에서 예매된 좌석인 bookList 요소를 제거하기 위한 함수
    for idx in range(len(x)):   # 예매한 좌석 목록은 str 형식으로 리스트에 저장 >> int 형식인 nobook 리스트와 비교하여 제거하기 위해
        x[idx] = int(x[idx])    # bookList의 요소들을 int형으로 변경
    for idx2 in range(len(x)):
        if x[idx2] in noBook:   # 만약 noBook 리스트에 예매한 좌석이 있는 경우에만 제거해줘야 함. 그렇지 않으면 잔여 좌석 확인마다 지워짐
            noBook.remove(x[idx2])  # >> 오류 발생
    for idx3 in range(len(x)):  # 비교를 위해 int형으로 전환한 bookList 항목들을 다시 str 형식으로 원상 복구
        x[idx3] = str(x[idx3])  # 다른 부분에서는 모두 str로 작동하게 코딩해놔서 꼭 해야 함.
