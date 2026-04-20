from collections import deque


class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(node):
    if node is None:
        return []
    queue = deque()
    queue.append(node)
    result = []
    while queue:
        nd = queue.popleft()
        result.append(nd.value)
        if nd.left is not None:
            queue.append(nd.left)
        if nd.right is not None:
            queue.append(nd.right)
    return result
