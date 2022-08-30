testcase = int(input())

for tc in range(1, testcase+1):

    input_list = list(input().split())

    N = int(input_list[0])

    B_idx = N*2
    O_idx = N*2
    B_finish = True
    O_finish = True

    for i in range(1, N*2, 2):
        if input_list[i] == 'B':
            if B_idx == N*2:
                B_idx = i
                B_destination = int(input_list[i+1])
                B_finish = False
        if input_list[i] == 'O':
            if O_idx == N*2:
                O_idx = i
                O_destination = int(input_list[i + 1])
                O_finish = False

    O = 1
    B = 1
    time = 0

    while not B_finish or not O_finish:
        if B_idx < O_idx:
            if not B_finish:
                if B == B_destination:
                    for i in range(B_idx + 2, N * 2, 2):
                        if input_list[i] == 'B':
                            B_idx = i
                            B_destination = int(input_list[B_idx+1])
                            break
                    else:
                        B_finish = True
                        B_idx = N*2
                elif B < B_destination:
                    B += 1
                elif B > B_destination:
                    B -= 1

            if not O_finish:
                if O == O_destination:
                    pass
                elif O < O_destination:
                    O += 1
                elif O > O_destination:
                    O -= 1

        elif O_idx < B_idx:
            if not O_finish:
                if O == O_destination:
                    for i in range(O_idx + 2, N * 2, 2):
                        if input_list[i] == 'O':
                            O_idx = i
                            O_destination = int(input_list[O_idx + 1])
                            break
                    else:
                        O_idx = N*2
                        O_finish = True
                elif O < O_destination:
                    O += 1
                elif O > O_destination:
                    O -= 1

            if not B_finish:
                if B == B_destination:
                    pass
                elif B < B_destination:
                    B += 1
                elif B > B_destination:
                    B -= 1

        time += 1

    print(f'#{tc} {time}')
