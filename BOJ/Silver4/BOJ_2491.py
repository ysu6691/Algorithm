# 연속으로 작아지는 숫자 수와 커지는 숫자 수를 따로 비교
# 둘 중 더 큰 수를 출력

N = int(input())

num_list = list(map(int, input().split()))

max_cnt = -1

i = 0
cnt = 1

# 연속으로 작아지는 숫자 수를 저장
while i < N - 1:
    if num_list[i] > num_list[i + 1]:
        if cnt > max_cnt:
            max_cnt = cnt
        cnt = 0 # 연속이 끊겼다면, 처음부터 세기
    i += 1 # 다음 인덱스로
    cnt += 1 

if cnt > max_cnt:
    max_cnt = cnt

i = 0
cnt = 1

# 연속으로 커지는 숫자 수를 저장
while i < N - 1:
    if num_list[i] < num_list[i + 1]:
        if cnt > max_cnt:
            max_cnt = cnt
        cnt = 0

    i += 1
    cnt += 1

if cnt > max_cnt:
    max_cnt = cnt

print(max_cnt)
