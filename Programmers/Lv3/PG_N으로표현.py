def solution(N, number):

    def calc(list1, list2):
        tmp_list = []
        for num1 in list1:
            for num2 in list2:
                if num1 + num2 not in memo:
                    tmp_list.append(num1 + num2)
                    memo.add(num1 + num2)
                if -(num1 + num2) not in memo:
                    tmp_list.append(-(num1 + num2))
                    memo.add(-(num1 + num2))
                if num1 - num2 not in memo:
                    tmp_list.append(num1 - num2)
                    memo.add(num1 - num2)
                if num1 * num2 not in memo:
                    tmp_list.append(num1 * num2)
                    memo.add(num1 * num2)
                if -(num1 * num2) not in memo:
                    tmp_list.append(-(num1 * num2))
                    memo.add(-(num1 * num2))
                if num2 and int(num1 / num2) not in memo:
                    tmp_list.append(int(num1 / num2))
                    memo.add(int(num1 / num2))
                if num2 and -int(num1 / num2) not in memo:
                    tmp_list.append(-int(num1 / num2))
                    memo.add(-int(num1 / num2))
        return tmp_list

    DP = [[] for _ in range(9)]
    memo = set()
    finish = False
    answer = -1

    for i in range(1, 9):
        DP[i].append(int(str(N)*i))
        memo.add(int(str(N)*i))
        DP[i].append(-int(str(N)*i))
        memo.add(-int(str(N)*i))
        if number in DP[i]:
            answer = i
            break
        for j in range(1, i):
            DP[i] += calc(DP[j], DP[i-j])
            if number in DP[i]:
                answer = i
                finish = True
                break
        if finish:
            break
            
    return answer
