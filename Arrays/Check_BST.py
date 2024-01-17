class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def CheckBST(self,root, min_value = float('-inf'), max_value = float('inf')):
    if root is None:
        return True
    if root.data <= min_value or root.data >= max_value:
        return False
    return (self.CheckBST(root.left, min_value, root.data) and self.CheckBST(root.right, root.data, max_value))



if __name__ == "__main__":
    root = Node(5)
    root.left = Node(3)
    root.right = Node(7)
    root.left.left = Node(2)
    root.right.left = Node(6)

    if (CheckBST(root)):
        print("True")
    else:
        print("Flase")
