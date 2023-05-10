import sys
input = sys.stdin.readline

N = int(input())
word_dict = dict()
word_set = set()
for _ in range(N):
    word = input().strip()
    if word in word_set:
        continue
    word_set.add(word)
    length = len(word)
    if length in word_dict:
        word_dict[length].append(word)
    else:
        word_dict[length] = [word]

answer = []
for n in range(1, 51):
    if n in word_dict:
        answer.extend(sorted(word_dict[n]))

for word in answer:
    print(word)