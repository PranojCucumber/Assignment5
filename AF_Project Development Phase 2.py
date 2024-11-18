class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, node, value):
        if value < node.value:
            if not node.left:
                node.left = TreeNode(value)
            else:
                self._add_recursive(node.left, value)
        elif value > node.value:
            if not node.right:
                node.right = TreeNode(value)
            else:
                self._add_recursive(node.right, value)

    def find(self, value):
        return self._find_recursive(self.root, value)

    def _find_recursive(self, node, value):
        if not node:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._find_recursive(node.left, value)
        else:
            return self._find_recursive(node.right, value)

    def inorder(self):
        results = []
        self._inorder_recursive(self.root, results)
        return results

    def _inorder_recursive(self, node, results):
        if node:
            self._inorder_recursive(node.left, results)
            results.append(node.value)
            self._inorder_recursive(node.right, results)

    def remove(self, value):
        self.root = self._remove_recursive(self.root, value)

    def _remove_recursive(self, node, value):
        if not node:
            return None
        if value < node.value:
            node.left = self._remove_recursive(node.left, value)
        elif value > node.value:
            node.right = self._remove_recursive(node.right, value)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            successor = self._min_value_node(node.right)
            node.value = successor.value
            node.right = self._remove_recursive(node.right, successor.value)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

# Test Cases
bst = BinarySearchTree()
bst.add(10)
bst.add(5)
bst.add(15)
bst.add(3)
bst.add(7)
print("Inorder traversal:", bst.inorder())
print("Find 7:", bst.find(7))
print("Find 12:", bst.find(12))
bst.remove(5)
print("Inorder traversal after removing 5:", bst.inorder())
