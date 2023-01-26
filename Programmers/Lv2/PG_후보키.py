def solution(relation):

    def comb(idx, sidx):
        if sidx == i:
            # 만든 조합이 현재 존재하는 후보키를 포함하는지 확인
            for candidate_key in candidate_keys:
                for j in range(1 << len(selection)):
                    tmp = []
                    for k in range(len(selection)):
                        if j & (1 << k):
                            tmp.append(selection[k])
                    if candidate_key == tuple(tmp):
                        return
            # 후보키를 포함하지 않는다면, 후보키로 가능한지 확인
            check = []
            for row in relation:
                row_comb = []
                for idx in selection:
                    row_comb.append(row[idx])
                if row_comb in check:
                    return
                check.append(row_comb)
            candidate_keys.add(tuple(selection))
            return

        if idx == tuple_num:
            return

        selection[sidx] = num_list[idx]
        comb(idx + 1, sidx + 1)
        comb(idx + 1, sidx)

    candidate_keys = set() # 후보키들
    tuple_num = len(relation[0]) # 총 튜플 수
    num_list = list(range(tuple_num)) # [0 ~ 튜플 수 - 1]
    # 1개부터 총 튜플 수까지 조합 생성
    for i in range(1, tuple_num + 1):
        selection = [0] * i
        comb(0, 0)

    answer = len(candidate_keys)
    return answer
