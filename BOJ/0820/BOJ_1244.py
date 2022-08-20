# 아이디어
# student 리스트에 [1, idx], [2, idx]와 같이 성별과 인덱스를 리스트로 저장
# 성별에 맞게 스위치 리스트 조작

# 스위치 함수
def switch(s_list, idx):
    if s_list[idx] == 0:
        s_list[idx] = 1
    elif s_list[idx] == 1:
        s_list[idx] = 0
    return

# 스위치 수 저장
N = int(input())

# 스위치 리스트의 0번째 인덱스에 -1 저장
# 1번째인덱스부터 차례대로 스위치 현황 저장
switch_list = [-1]
switch_list.extend(list(map(int, input().split())))

# 학생 수 저장
students = int(input())

student_list = []

for i in range(students):
    student_list.append(list(map(int, input().split())))

# 남학생이면, 배수에 맞게 스위치 조작
# 여학생이면, 대칭 확인 후 스위치 조작
for i in student_list:
    if i[0] == 1:
        j = i[1]
        while j <= N:
            switch(switch_list, j)
            j += i[1]

    elif i[0] == 2:
        left = i[1] - 1
        right = i[1] + 1
        switch(switch_list, i[1])

        while left > 0 and right < N+1:
            if switch_list[left] == switch_list[right]:
                switch(switch_list, left)
                switch(switch_list, right)
                left -= 1
                right += 1
            else:
                break

# 0번 인덱스를 제외하고, 1~20, 21~40, ... 범위의 리스트가 존재하면 출력
for i in range(5):
    if switch_list[i * 20 + 1: i * 20 + 21]:
        print(' '.join(list(map(str, switch_list[i * 20 + 1 : i * 20 + 21]))))
    else:
        break
