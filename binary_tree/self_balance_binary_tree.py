class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def rightRotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))

        return x

    def leftRotate(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def insert(self, node, key):
        # 1. Normal BST insert
        if not node:
            return Node(key)
        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        # 2. Update height
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))

        # 3. Get balance
        balance = self.getBalance(node)

        # 4. Balance the tree
        # Case 1: Left Left
        if balance > 1 and key < node.left.key:
            return self.rightRotate(node)

        # Case 2: Right Right
        if balance < -1 and key > node.right.key:
            return self.leftRotate(node)

        # Case 3: Left Right
        if balance > 1 and key > node.left.key:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        # Case 4: Right Left
        if balance < -1 and key < node.right.key:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node

    def preOrder(self, root):
        if root:
            print(root.key, end=" ")
            self.preOrder(root.left)
            self.preOrder(root.right)




tree = AVLTree()
root = None

for key in [10, 20, 30, 40, 50, 25]:
    root = tree.insert(root, key)

tree.preOrder(root)  # Output: 30 20 10 25 40 50