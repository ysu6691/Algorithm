def solution(answers):

    one_list = [1,2,3,4,5]
    two_list = [2,1,2,3,2,4,2,5]
    three_list = [3,3,1,1,2,2,4,4,5,5]

    one = 0
    two = 0
    three = 0

    one_cnt = 0
    two_cnt = 0
    three_cnt = 0

    while answers:

        answer = answers.pop(0)

        if answer == one_list[one % 5]:
            one_cnt += 1

        if answer == two_list[two % 8]:
            two_cnt += 1

        if answer == three_list[three % 10]:
            three_cnt += 1

        one += 1
        two += 1
        three += 1

    cnt_list = [one_cnt, two_cnt, three_cnt]
    max_cnt = max(cnt_list)



    answer = []
    for i in range(3):
        if cnt_list[i] == max_cnt:
            answer.append(i+1)

    return answer