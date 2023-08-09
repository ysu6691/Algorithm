def solution(distance, rocks, n):
    
    rocks.sort()
    rocks.insert(0, 0)
    rocks.append(distance)
    left = 1
    right = distance
    answer = 0
    
    while left <= right:
        middle = (left + right) // 2
        remove_rock_cnt = 0
        left_idx = 0
        right_idx = 1
        
        while right_idx < len(rocks):
            # print(left_idx, right_idx, remove_rock_cnt)
            if rocks[right_idx] - rocks[left_idx] < middle:
                remove_rock_cnt += 1
                right_idx += 1
                if remove_rock_cnt > n:
                    right = middle - 1
                    break
            else:
                left_idx = right_idx
                right_idx += 1
        else:
            if middle > answer:
                answer = middle
            left = middle + 1
                
    return answer