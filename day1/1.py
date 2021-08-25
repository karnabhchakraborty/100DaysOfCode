# BFS traversal of a tree

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def BFS(root):
        if root is None:
            return

        queue = []
        queue.append(root)

        while len(queue) > 0:
            top = queue.pop(0)
            print(top.val)

            if top.left:
                queue.append(top.left)
            if top.right:
                queue.append(top.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print ("Level Order Traversal of binary tree is -")
Node.BFS(root)