# 힙 정렬하는 함수
def heapify(idx):
    # 만약 자식 노드가 부모 노드보다 작다면, 자리 바꾸기
    if heap[idx] < heap[idx//2]:
        heap[idx], heap[idx//2] = heap[idx//2], heap[idx]
        heapify(idx//2) # 부모 노드로 이동

testcase = int(input())

for tc in range(1, testcase+1):
    N = int(input())
    num_list = list(map(int, input().split()))

    heap = [0]
    idx = 0

    # heap에 숫자 넣고, 정렬 수행
    for n in num_list:
        heap.append(n)
        idx += 1 # 인덱스 1씩 늘려주기
        heapify(idx)

    # 조상 노드 모두 더하기
    result = 0
    while idx > 0:
        idx //= 2
        result += heap[idx]

    print(f'#{tc} {result}')