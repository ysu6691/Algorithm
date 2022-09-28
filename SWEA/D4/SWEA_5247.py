testcase = int(input())

for tc in range(1, testcase+1):

    N, M = map(int, input().split())
    # num_list의 n번째 인덱스 리스트는 n번 연산했을 때 만들 수 있는 숫자 모음
    num_list = [[N]] # 0번 연산했을 때 만들 수 있는 숫자는 N 하나뿐
    memo = {N} # 연산해서 나왔던 숫자 기억

    cnt = 1

    while True:
        num_list.append([]) # 다음 연산으로
        for num in num_list[cnt-1]: # 이전 연산만 보면 됨
            # 연산 후 이미 나왔던 숫자가 아니면, 기억하기
            if num + 1 not in memo and num + 1 <= 1000000:
                num_list[cnt].append(num+1)
                memo.add(num+1)
            if num - 1 not in memo and num - 1 <= 1000000:
                num_list[cnt].append(num-1)
                memo.add(num-1)
            if num * 2 not in memo and num * 2 <= 1000000:
                num_list[cnt].append(num*2)
                memo.add(num*2)
            if num - 10 not in memo and num - 10 <= 1000000:
                num_list[cnt].append(num-10)
                memo.add(num-10)

        # 원하는 숫자 찾았으면 break
        if M in num_list[cnt]:
            break

        # 다음 연산으로
        cnt += 1

    print(f'#{tc} {cnt}')