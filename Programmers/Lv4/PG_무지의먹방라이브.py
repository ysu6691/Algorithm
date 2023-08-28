def solution(food_times, k):
    
    time_dict = dict()
    for time in food_times:
        if time in time_dict:
            time_dict[time] += 1
        else:
            time_dict[time] = 1
    
    sorted_times = sorted(food_times)
    size = len(food_times)
    time_memo = set()
    before_time = 0
    for time in sorted_times:
        if time in time_memo:
            continue
        time_memo.add(time)
        if k - (time - before_time) * size < 0:
            break
        k -= (time - before_time) * size
        size -= time_dict[time]
        before_time = time
    else:
        return -1

    k %= size
    
    for idx in range(len(food_times)):
        current = food_times[idx]
        if current >= time:
            k -= 1
            if k < 0:
                return idx + 1
            
    
