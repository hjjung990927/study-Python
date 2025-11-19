# 각 인덱스는 서로 공유한다.

# 상품명 저장소
name_list = []
# 가격 저장소
price_list = []

title = ""
menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n"
search_menu = "1.상품명으로 검색\n2.가격으로 검색\n"
append_message = '추가하실 상품명과 가격을 입력하세요.\n예)상품명 가격'
search_name_message_for_update = '수정하실 상품명을 입력하세요.'
update_message = '새로운 상품명과 가격을 입력하세요.\n예)상품명 가격'
delete_message = '삭제하실 상품명을 입력하세요.'
search_name_message, search_price_message = '상품명: ', '가격: '

append_error_message = "추가 실패(중복된 상품명)"
update_error_message = "수정 실패(존재하지 않는 상품명)"
delete_error_message = "삭제 실패(존재하지 않는 상품명)"
search_name_error_message = "검색 실패(존재하지 않는 상품명)"
search_error_message = "검색 결과가 없습니다."
error_message = "다시 입력해주세요."
no_item_message = "목록이 없습니다."

while True:
    choice = int(input(title + "\n" + menu))

    # 추가
    if choice == 1:
        # 동시에 상품명과 가격을 입력받은 뒤 공백을 구분하여 각 변수에 담아준다.
        new_name, new_price = input(append_message).split(" ")
        # 기존에 상품명이 없다면
        if new_name not in name_list:
            # 마지막에 각각 추가한다.
            name_list.append(new_name)
            price_list.append(int(new_price))
        else:
            # 만약 상품명이 중복되면 오류 메세지 출력
            print(append_error_message)
    # 수정
    elif choice == 2:
        # 수정할 상품의 이름을 입력받는다.
        name = input(search_name_message_for_update)
        # 해당 상품이 존재하면
        if name in name_list:
            # 그 상품의 인덱스를 찾는다.
            index = name_list.index(name)
            # 사용자에게 새로운 상품명과 새로운 가격을 입력받는다.
            new_name, new_price = input(update_message).split(" ")
            # 기존 위치에 새로운 정보로 갱신한다.
            name_list[index] = new_name
            price_list[index] = new_price
        else:
            print(update_error_message)
    # 삭제
    elif choice == 3:
        # 삭제할 상품명을 입력받는다.
        name = input(delete_message)
        # 해당 상품이 존재하면
        if name in name_list:
            # 상품명이 아닌 가격부터 삭제해주고
            del price_list[name_list.index(name)]
            # 이후 상품명을 삭제해줘야 정상적으로 모두 삭제된다.
            name_list.remove(name)

        else:
            print(delete_error_message)

    # 검색
    elif choice == 4:
        choice = int(input(search_menu))
        # 상품명으로 검색
        if choice == 1:
            # 상품명을 입력받고
            name = input(search_name_message)
            # 존재하면
            if name in name_list:
                # 해당 상품의 인덱스를 가져온다.
                index = name_list.index(name)
                # 해당 상품의 정보를 출력한다.
                print(f'{name_list[index]} - {price_list[index]}')
            else:
                print(search_name_error_message)

        # 가격으로 검색
        elif choice == 2:
            check = False
            # 사용자가 입력한 가격에서 오차 범위 ±50%로 조회한다.
            price = int(input(search_price_message))
            min = price * 0.5
            max = price * 1.5

            # 모든 가격을 가져와서
            for i in range(len(price_list)):
                # 해당 범위 내에 있는지 검사한다.
                if min <= price_list[i] <= max:
                    # 만약 한 개라도 해당 범위에 들어온다면 Flag에 True를 담아준다.
                    check = True
                    # 해당 상품 정보를 출력해준다.
                    print(f'{name_list[i]} - {price_list[i]}')

            # 조회된 상품이 없으면
            if not check:
                # 해당 메세지를 출력해준다.
                print(search_error_message)

        # 그 외
        else:
            print(error_message)

    # 목록
    elif choice == 5:
        # 상품이 없으면
        if len(name_list) == 0:
            # 없다고 출력해준다.
            print(no_item_message)
            # 아래의 반복문으로 가지 않도록 막아준다.
            continue

        # 상품이 1개라도 있으면, 모든 정보 출력
        for i in range(len(name_list)):
            print(f'{name_list[i]} - {price_list[i]}')

    # 나가기
    elif choice == 6:
        break

    # 그 외
    else:
        print(error_message)