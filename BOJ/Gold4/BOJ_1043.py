def findset(n):
    if n != parent[n]:
        return findset(parent[n])
    return parent[n]

def union(n1, n2):
    n1 = findset(n1)
    n2 = findset(n2)
    if n1 in know_set:
        parent[n2] = n1
    elif n2 in know_set:
        parent[n1] = n2
    else:
        parent[n2] = n1

###########################################

N, M = map(int, input().split())
know_info = list(map(int, input().split()))
know_set = set(know_info[1:])
parent = list(range(N+1))
memo = []

for i in range(M):
    people_info = list(map(int, input().split()))
    go_next = False
    memo.append(people_info[1:])
    for person in people_info[1:]:
        union(people_info[1], person)

answer = 0
for i in memo:
    flag = False
    for person in i:
        if findset(person) in know_set:
            flag = True
            break
    else:
        answer += 1

    if flag:
        for person in i:
            know_set.add(person)

print(answer)
