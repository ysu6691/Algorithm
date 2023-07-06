def solution(words):
    
    trie = dict()
    
    for word in words:
        current_trie = trie
        for idx in range(len(word)):
            if word[idx] in current_trie:
                current_trie[word[idx]][1] += 1
                current_trie[word[idx]][2] = idx + 1
                current_trie = current_trie[word[idx]][0]
            else:
                current_trie[word[idx]] = [dict(), 1, idx + 1]
                current_trie = current_trie[word[idx]][0]
    
    answer = 0
    for word in words:
        current_trie = trie
        for idx in range(len(word)):
            current_list = current_trie[word[idx]]
            if current_list[1] == 1:
                answer += idx + 1
                break
            current_trie = current_list[0]
        else:
            answer += len(word)
            
    return answer