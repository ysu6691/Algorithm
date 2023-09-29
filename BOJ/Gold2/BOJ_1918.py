import sys
input = sys.stdin.readline

string = input().rstrip()
answer = ""
stack = []
priority_dict = {"+": {"+", "-", "*", "/"},
                 "-": {"+", "-", "*", "/"},
                 "*": {"*", "/"},
                 "/": {"*", "/"},
                 "(": {},
                }

for i in range(len(string)):
    if string[i] in {"+", "-", "*", "/", "("}:
        while stack and stack[-1] in priority_dict[string[i]]:
            answer += stack.pop()
        stack.append(string[i])
    elif string[i] == ")":
        while stack[-1] != "(":
            answer += stack.pop()
        stack.pop()
    else:
        answer += string[i]

while stack:
    answer += stack.pop()

print(answer)