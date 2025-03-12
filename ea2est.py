class Node:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None
        self.height = 1


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, label):
        self.root = self._insert(self.root, label)

    def _insert(self, node, label):
        if not node:
            return Node(label)

        if label < node.label:
            node.left = self._insert(node.left, label)
        else:
            node.right = self._insert(node.right, label)

        return self._balance(node)

    def remove(self, label):
        self.root = self._remove(self.root, label)

    def _remove(self, node, label):
        if not node:
            return node

        if label < node.label:
            node.left = self._remove(node.left, label)
        elif label > node.label:
            node.right = self._remove(node.right, label)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self._get_min_value_node(node.right)
            node.label = temp.label
            node.right = self._remove(node.right, temp.label)

        return self._balance(node)

    def _get_min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    def _balance(self, node):
        if not node:
            return node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)

        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)

        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _get_height(self, node):
        return node.height if node else 0

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

    def in_order(self):
        self._in_order(self.root)
        print()

    def _in_order(self, node):
        if node:
            self._in_order(node.left)
            print(node.label, end=" ")
            self._in_order(node.right)


# Teste
avl = Tree()
avl.insert(10)
avl.insert(30)
avl.insert(90)
avl.insert(20)
avl.insert(40)
avl.insert(60)
avl.insert(80)

print("Árvore AVL em ordem:")
avl.in_order()

avl.remove(40)
print("Árvore AVL após remover 40:")
avl.in_order()