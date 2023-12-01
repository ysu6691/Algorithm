import sys
sys.setrecursionlimit(10**5)

def solution(nodeinfo):
    
    def find_parent(left, right, depth, parent_node):
        if depth == len(nodes) or left >= right:
            return
        
        start = 0
        end = len(nodes[depth]) - 1
        while start < end:
            middle = (start + end) // 2
            if parent_node == 4 and left == 3:
                print(middle)
            if nodes[depth][middle][1] > right:
                end = middle
            elif nodes[depth][middle][1] < left:
                start = middle + 1
            elif left <= nodes[depth][middle][1] <= right:
                start = middle
                break
        
        current_node = nodes[depth][start][0]
        current_x = nodes[depth][start][1]
        
        if left <= current_x <= right:
            parent[current_node] = parent_node
            children[parent_node].append(current_node)
            find_parent(left, current_x, depth + 1, current_node)
            find_parent(current_x, right, depth + 1, current_node)
            
    
    def preorder(node):
        answer[0].append(node)
        for child in children[node]:
            if node != child:
                preorder(child)
                
    
    def postorder(node):
        for child in children[node]:
            if node != child:
                postorder(child)
        answer[1].append(node)
        
    
    n = len(nodeinfo)
    for i in range(n):
        nodeinfo[i].append(i + 1)
    
    nodeinfo.sort(key=lambda x: x[1], reverse=True)
    nodes = [[]]
    current_height = nodeinfo[0][1]
    current_depth = 0
    min_x = 100001
    max_x = -1
    for node in nodeinfo:
        if node[1] == current_height:
            nodes[current_depth].append((node[2], node[0]))
        else:
            nodes.append([(node[2], node[0])])
            current_depth += 1
            current_height = node[1]
        max_x = max(max_x, node[0])
        min_x = min(min_x, node[0])
    
    for node_list in nodes:
        node_list.sort(key=lambda x: x[1])
    
    parent = list(range(n + 1))
    root_node = nodes[0][0][0]
    root_x = nodes[0][0][1]
    children = [[] for _ in range(len(nodeinfo) + 1)]
    find_parent(min_x, max_x, 0, root_node)
    
    answer = [[], []]
    preorder(root_node)
    postorder(root_node)
    
    return answer