N, Q = map(int, input().split())
nodes = [0]*(N+1)
result = []

for _ in range(Q):
    start = int(input())
    node = start
    finish = False
    while True:
        if not nodes[node]:
            node //= 2
        else:
            while node > 1:
                if nodes[node]:
                    memo = node
                node //= 2
            result.append(memo)
            finish = True

        if finish:
            break

        if node == 1:
            nodes[start] = 1
            result.append(0)
            break

for i in result:
    print(i)