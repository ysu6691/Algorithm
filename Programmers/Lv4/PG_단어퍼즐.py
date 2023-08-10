from collections import deque

def solution(strs, t):

    trie = dict()
    for idx in range(len(strs)):
        word = strs[idx]
        current_trie = trie
        for char in word:
            if char in current_trie:
                current_trie = current_trie[char]
            else:
                current_trie[char] = dict()
                current_trie = current_trie[char]
        current_trie["finish"] = 1
        
    answer = 987654321
    memo = [987654321] * len(t)
    queue = deque([(0, 0)])
    
    while queue:
        idx, cnt = queue.popleft()
        current_trie = trie
        
        if t[idx] in trie:
            current_trie = trie[t[idx]]
            tmp_cnt = 1
            while True:
                if idx + tmp_cnt == len(t):
                    if "finish" in current_trie and cnt + 1 < answer:
                        answer = cnt + 1
                    break
                if "finish" in current_trie and memo[idx + tmp_cnt] > cnt + 1:
                    queue.append((idx + tmp_cnt, cnt + 1))
                    memo[idx + tmp_cnt] = cnt + 1
                if t[idx + tmp_cnt] in current_trie:
                    current_trie = current_trie[t[idx + tmp_cnt]]
                else:
                    break
                tmp_cnt += 1
            
    if answer == 987654321:
        answer = -1
        
    return answer