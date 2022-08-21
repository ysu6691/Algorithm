# 아이디어
# 2중 for문 돌리면 시간초과
# while문을 돌면서 맨 앞 인덱스 값을 빼주고 맨 뒤 + 1 인덱스 값을 더해줌

N, K = map(int, input().split())

temp = list(map(int, input().split()))

i = 0
j = K

sum_temp = sum(temp[i:j])
max_sum = sum_temp

while j < N:
    sum_temp -= temp[i]
    sum_temp += temp[j]
    if sum_temp > max_sum:
        max_sum = sum_temp

    i += 1
    j += 1

print(max_sum)
