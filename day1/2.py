# DFS traversal of a tree

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def DFS(self,root):
        if root:
            self.DFS(self,root.left)
            print(root.val)
            self.DFS(self,root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print ("Level Order Traversal of binary tree is -")
Node.DFS(Node,root)