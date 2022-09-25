def preorder(n):
    if n:
        preorder_visited.append(chr(n+64))
        preorder(left[n])
        preorder(right[n])

def inorder(n):
    if n:
        inorder(left[n])
        inorder_visited.append(chr(n+64))
        inorder(right[n])

def postorder(n):
    if n:
        postorder(left[n])
        postorder(right[n])
        postorder_visited.append(chr(n+64))


N = int(input())
left = [0]*27
right = [0]*27

for _ in range(N):
    p, c1, c2 = input().split()
    p = ord(p) - 64
    if 65 <= ord(c1) <= 90:
        c1 = ord(c1) - 64
        left[p] = c1
    if 65 <= ord(c2) <= 90:
        c2 = ord(c2) - 64
        right[p] = c2

preorder_visited = []
inorder_visited = []
postorder_visited = []

preorder(1)
inorder(1)
postorder(1)

print(''.join(preorder_visited))
print(''.join(inorder_visited))
print(''.join(postorder_visited))
