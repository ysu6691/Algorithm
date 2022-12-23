testcase = int(input())
for _ in range(testcase):
    N = int(input())
    people = input()
    people_dict = dict()
    people_num_dict = dict()

    # 그룹의 인원수와 가장 마지막에 나온 사람의 인덱스를 기억
    for idx in range(N):
        person = people[idx]
        people_dict[person] = idx + 1
        if person in people_num_dict:
            people_num_dict[person] += 1
        else:
            people_num_dict[person] = 1

    # 가장 마지막에 나온 사람의 인덱스를 오름차순으로 정렬 (가장 먼저 리프트를 탈 수 있는 그룹 순으로)
    people_list = sorted(people_dict.items(), key=lambda x: x[1])

    """
    print(people_dict)     # {'A': 5, 'b': 8, '9': 3, '2': 10, 'C': 9}
    print(people_num_dict) # {'A': 3, 'b': 3, '9': 1, '2': 2, 'C': 1}
    print(people_list)     # [('9', 3), ('A', 5), ('b', 8), ('C', 9), ('2', 10)]
    """

    answer = 0
    idx = 0
    for people in people_list:
        # 인원 수만큼 인덱스 뛰기
        idx += people_num_dict[people[0]]
        # (원래 인덱스 - 현재 인덱스) * 그룹 내 인원 수 * 5
        answer += (people_dict[people[0]] - idx) * people_num_dict[people[0]] * 5

    print(answer)