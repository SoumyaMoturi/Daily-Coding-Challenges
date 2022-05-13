'''
This problem was asked by Google.

Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

    a
   / \
  b   c
 /
d

'''
class Node:
    def __init__(self,data):
        self.data = data
        self.right = self.left = None
def findheight(root):
    if not root:
        return 0;
    left_height = findheight(root.left)
    right_height = findheight(root.right)
    return max(left_height,right_height)+1
def deepestNode(root,levels):
    if root == None:
        return ''
    if levels == 1:
        print("The deepest Node of given Binary tree : "+ root.data)
    elif(levels>1):
        deepestNode(root.left,levels-1)
        deepestNode(root.right,levels-1)
if __name__ == "__main__":
    root = Node('a')
    root.left = Node('b')
    root.right = Node('c')
    root.left.left = Node('d')
    height = findheight(root)
    deepestNode(root,height)