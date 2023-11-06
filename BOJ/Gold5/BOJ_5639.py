import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def make_postorder(left, right):

    if left > right:
        return []

    if left == right:
        return [nodes[left]]

    for i in range(left + 1, right + 1):
        if nodes[i] > nodes[left]:
            return make_postorder(left + 1, i - 1) + make_postorder(i, right) + [nodes[left]]
    return make_postorder(left + 1, right) + [nodes[left]]

nodes = []
while True:
    try:
        num = int(input())
        nodes.append(num)
    except:
        break

postorder = make_postorder(0, len(nodes) - 1)
for num in postorder:
    sys.stdout.write(str(num) + "\n")
sys.stdout.flush()

