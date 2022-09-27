testcase = int(input())

for tc in range(1, testcase+1):
    N, K = map(int, input().split())
    nums = list(input())
    result = set() # 중복 피하기 위해 set으로 생성

    # N//4번만큼 돌리기
    for i in range(N//4):
        nums.append(nums.pop(0))

        # 변을 돌면서, 숫자 조합 하나씩 받아오기
        for j in range(0, N, N//4):
            num = nums[j:j+N//4]

            # 16진수를 10진수로 변환
            for k in range(len(num)):
                if 65 <= ord(num[k]) <= 70: # 알파벳은 숫자로 바꾸기
                    num[k] = ord(num[k]) - 55
            tmp = 0
            order = 0
            for k in num[::-1]: # 끝에서부터 16^0, 16^1, 16^2 만큼 곱해줘야 함
                tmp += (16**order) * int(k)
                order += 1
            result.add(tmp)

    # 내림차순 정렬
    result = list(result)
    result.sort(reverse=True)

    print(f'#{tc} {result[K-1]}')