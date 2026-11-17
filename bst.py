class BSTNode:
    def __init__(self, key, name):
        self.key = key
        self.name = name
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key, name):
        if root is None:
            return BSTNode(key, name)
        if key < root.key:
            root.left = self.insert(root.left, key, name)
        elif key > root.key:
            root.right = self.insert(root.right, key, name)
        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def inorder(self, root):                        # Sorted traversal: Left -> Root -> Right
        if root:
            self.inorder(root.left)
            print(f"{root.key}: {root.name}")
            self.inorder(root.right)

    def get_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:                   # 0 or 1 right child
                return root.right
            elif root.right is None:                # 1 left child
                return root.left
            temp = self.get_min(root.right)         # 2 children: replace with inorder successor
            root.key, root.name = temp.key, temp.name
            root.right = self.delete(root.right, temp.key)
        return root
