# 실패한 방법
# 시간 줄이려고 heapq 사용
import heapq

def solution(a):
    
    def find_last_balloon(left, right, direction):
        nonlocal answer
        
        if not a[left:right]:
            return
        
        answer += 1
        
        copied_array = a[left:right]
        heapq.heapify(copied_array) # 함수 돌 때마다 결국 O(N)만큼의 시간 소요
        min_num = heapq.heappop(copied_array)
        idx = idx_dict[min_num]
        
        if direction == "left":
            find_last_balloon(left, idx, "left")
        else:
            find_last_balloon(idx+1, right, "right")
    
    idx_dict = dict()
    min_num = 1000000001
    for i in range(len(a)):
        num = a[i]
        idx_dict[num] = i
        if num < min_num:
            min_num = num
            min_idx = i
    
    answer = 1
    find_last_balloon(0, min_idx, "left")
    find_last_balloon(min_idx + 1, len(a), "right")
    
    
    return answer

#######################################################

# 설공한 방법
def solution(a):

    # 최솟값과 인덱스 찾기
    min_num = 1000000001
    for i in range(len(a)):
        if a[i] < min_num:
            min_num = a[i]
            min_idx = i
    
    answer = 1

    # 왼쪽부터 보면서 현재까지의 최솟값 찾기
    left_min = 1000000001
    for i in range(min_idx):
        if a[i] < left_min:
            left_min = a[i]
            answer += 1 # 찾을 때마다 answer + 1
    
    # 오른쪽부터 보면서 현재까지의 최솟값 찾기
    right_min = 1000000001
    for i in range(len(a) - 1, min_idx, -1):
        if a[i] < right_min:
            right_min = a[i]
            answer += 1 # 찾을 때마다 answer + 1
    
    return answer