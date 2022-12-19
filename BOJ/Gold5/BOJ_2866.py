R, C = map(int, input().split())
word_list = [[] for _ in range(C)]

# 전치해서 리스트에 문자 하나씩 저장
for _ in range(R):
    row = input()
    for i in range(C):
        word_list[i].append(row[i])
# ex) 3 4
#     alfa
#     beta
#     zeta
#     word_list = [['a', 'b', 'z'], ['l', 'e', 'e'], ['f', 't', 't'], ['a', 'a', 'a']]

# 각 리스트의 문자 합치기
new_word_list = []
for word in word_list:
    new_word = ''.join(word)
    new_word_list.append(new_word)

# new_word_list = ['abz', 'lee', 'ftt', 'aaa']

answer = -1
finish = False
while True:
    word_set = set()
    for i in range(C):
        # 이미 있는 단어면 종료
        if new_word_list[i] in word_set:
            finish = True
            break
        # 나온 단어 기억하기
        word_set.add(new_word_list[i])
        # 기억한 뒤 슬라이싱
        new_word_list[i] = new_word_list[i][1:]
    # 중복된 단어를 못 찾으면 다음으로
    else:
        answer += 1
    # 중복된 단어가 있거나 마지막 행까지 모두 봤으면 종료
    if finish or not new_word_list[0]:
        break

print(answer)