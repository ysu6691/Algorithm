# N보다 작은 모든 값에 대해 규칙에 맞는 함수 실행
# 전값에서 다음값을 빼는 것을 반복하면서 카운트 추가
# 다음값이 그 차이보다 커지면, 함수 종료하고 카운트 반환

def rule(before, after, cnt):

    # 수가 더 커지면 cnt반환하고 함수 종료
    if before < after:
        tmp_list.append(after)
        return cnt

    # 리스트에 다음 값 추가
    tmp_list.append(after)

    # 다음 값부터 다시 함수 실행
    return rule(after, before - after, cnt+1)


N = int(input())

num = 0

max_cnt = 0

# N보다 작은 모든 수에 대해 모두 확인
while N >= num:
    # 리스트에는 N 넣고 시작
    tmp_list = [N]

    # 카운트는 2부터 시작
    tmp_cnt = rule(N, num, 2)

    # 카운트가 최대라면, 그때의 리스트 저장
    if tmp_cnt > max_cnt:
        max_cnt = tmp_cnt
        result = tmp_list[:] 

    num += 1

print(max_cnt)
print(' '.join(map(str, result)))