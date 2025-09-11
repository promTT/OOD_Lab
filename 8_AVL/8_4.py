class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
            self.h = 0  # ความสูงเริ่มต้น

        def update_height(self):
            left_h = self.left.h if self.left else -1
            right_h = self.right.h if self.right else -1
            self.h = 1 + max(left_h, right_h)

        def balanceValue(self):
            left_h = self.left.h if self.left else -1
            right_h = self.right.h if self.right else -1
            return left_h - right_h

    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if not self.root:
            self.root = BST.Node(key)
        else:
            self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return BST.Node(key)

        if key < node.data:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        # อัปเดตความสูงทุกครั้งหลัง insert
        node.update_height()
        return node

    def _get_format(root, ans=""):
        if root:
            temp = ""
            if root.right:
                temp += BST._get_format(root.right, ans + "     ")
            temp += f"{ans}{root.data}\n"
            if root.left:
                temp += BST._get_format(root.left, ans + "     ")
            return temp
        return ""
    
    def __str__(self):
        return BST._get_format(self.root)




################################
'''
⠀⠀⢘⣾⣾⣿⣾⣽⣯⣼⣿⣿⣴⣽⣿⣽⣭⣿⣿⣿⣿⣿⣧
⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⣰⣯⣾⣿⣿⡼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿
⠀⠀⠛⠛⠋⠁⣠⡼⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁
⠀⠀⠀⠤⣶⣾⣿⣿⣿⣦⡈⠉⠉⠉⠙⠻⣿⣿⣿⣿⣿⠿⠁⠀
⠀⠀⠀⠀⠈⠟⠻⢛⣿⣿⣿⣷⣶⣦⣄⠀⠸⣿⣿⣿⠗⠀⠀⠀
⠀⠀⠀⠀⠀⣼⠀⠄⣿⡿⠋⣉⠈⠙⢿⣿⣦⣿⠏⡠⠂⠀⠀⠀
⠀⠀⠀⠀⢰⡌⠀⢠⠏⠇⢸⡇⠐⠀⡄⣿⣿⣃⠈⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⣻⣿⢫⢻⡆⡀⠁⠀⢈⣾⣿⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣿⣻⣷⣾⣿⣿⣷⢾⣽⢭⣍⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⣿⣿⣿⡿⠈⣹⣾⣿⡞⠐⠁⠀⠀⠀⠁⠀⠀⠀
⠀⠀⠀⠨⣟⣿⢟⣯⣶⣿⣆⣘⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡆⠀⠐⠶⠮⡹⣸⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''

def isAVL(node: BST.Node):
    if not node:
        return True
    if abs(node.balanceValue()) > 1:
        return False
    return isAVL(node.left) and isAVL(node.right)

################################


tree = BST()

print("**********IsAVL**********")
for i in list(map(int, input("Enter numbers to insert in the tree: ").split())):
    tree.insert(i)
print("Tree:")
print(tree)
print("Is AVL???:", isAVL(tree.root))