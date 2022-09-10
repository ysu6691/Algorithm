# 순열 돌리면서, 6개의 줄 중 하나라도 26을 넘어간다면 백트래킹

arr = [list(input()) for _ in range(5)]
alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
num_list = [] # 위에서부터 알파벳에 해당하는 숫자 채울 리스트

cnt = 0

for i in range(5):
    for j in range(9):
        if arr[i][j] == 'x':
            cnt += 1  # x 개수 세기
            num_list.append(0) # 비어있는 자리는 0으로 채우기

        elif arr[i][j] in alphabet_list:
            alphabet_list.remove(arr[i][j]) # 채워야 하는 알파벳 구하기
            num_list.append(ord(arr[i][j]) - 64) # 채워져 있는 자리는 해당 숫자로 채우기

# num_list = [0, 1, 9, 4, 0, 0, 0, 0, 0, 0, 0, 0]
# ....x....         ....0....
# .A.I.D.x.         .1.9.4.x.
# ..x...x..     ->  ..0...0..
# .x.x.x.x.         .0.0.0.0.
# ....x....         ....0....
# alphabet_list = ['B', 'C', 'E', 'F', 'G', 'H', 'J', 'K', 'L']

finish = False

def perm(depth):
    global finish
    if depth == cnt:
        perm_list.append(selection[:])
        finish = True
        return

    # 순열은 가장 낮은 알파벳부터 채워지므로,
    # 조건에 맞는 순열을 하나 찾았다면, 그만 찾아도 됨
    if finish:
        return

    for i in range(cnt):
        if not check[i]:
            check[i] = 1
            selection[depth] = alphabet_list[i]
            # 위에서부터 빈 자리 채우기
            for j in range(12):
                if not num_list[j]:
                    num_list[j] = ord(selection[depth]) - 64
                    break # 자리 채웠다면 break
                    
            # 각 줄을 각각 더해 26이 넘어가면 백트래킹
            if num_list[0] + num_list[2] + num_list[5] + num_list[7] > 26:
                check[i] = 0
                num_list[j] = 0
                return
            if num_list[0] + num_list[3] + num_list[6] + num_list[10] > 26:
                check[i] = 0
                num_list[j] = 0
                return
            if num_list[7] + num_list[8] + num_list[9] + num_list[10] > 26:
                check[i] = 0
                num_list[j] = 0
                return
            if num_list[1] + num_list[2] + num_list[3] + num_list[4] > 26:
                check[i] = 0
                num_list[j] = 0
                return
            if num_list[1] + num_list[5] + num_list[8] + num_list[11] > 26:
                check[i] = 0
                num_list[j] = 0
                return
            if num_list[4] + num_list[6] + num_list[9] + num_list[11] > 26:
                check[i] = 0
                num_list[j] = 0
                return

            perm(depth+1)
            check[i] = 0
            num_list[j] = 0

check = [0] * cnt
selection = [0] * cnt
perm_list = []
perm(0)

# perm_list = [['F', 'L', 'H', 'E', 'C', 'J', 'B', 'K', 'G']]
# result = ['F', 'L', 'H', 'E', 'C', 'J', 'B', 'K', 'G']
result = perm_list[0]

# result에서 앞에서부터 하나씩 빼와서 빈자리 채우기
for i in range(5):
    for j in range(9):
        if arr[i][j] == 'x':
            arr[i][j] = result.pop(0)

for i in range(5):
    print(''.join(arr[i]))
