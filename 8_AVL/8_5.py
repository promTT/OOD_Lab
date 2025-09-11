class AVLTree:
    def __init__(self):
        self.root = None

    def insertMovie(self, movie):  
        self.root = self._insert(self.root, movie)

    def _insert(self, node, movie):
        if not node:
            return Node(Movie(movie[0], movie[1]))
        
        if movie[1] < node.movies[0].rating:
            node.left = self._insert(node.left, movie)
        elif movie[1] > node.movies[0].rating:
            node.right = self._insert(node.right, movie)
        else:
            if not any(m.title == movie[0] for m in node.movies):
                node.movies.append(Movie(movie[0], movie[1]))
        
        node.setHeight()
        return self.balance(node)

    def removeMovie(self, movieName):
        self.root = self._remove(self.root, movieName)

    def _remove(self, node, movieName):
        if not node:
            return node

        found = False
        for i, m in enumerate(node.movies):
            if m.title == movieName:
                del node.movies[i]
                found = True
                break
        if found:
            if not node.movies:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    succ = self.getMin(node.right)
                    node.movies = succ.movies.copy()
                    node.right = self._remove(node.right, succ.movies[0].title)
            node.setHeight()
            return self.balance(node)
        
        if node.left:
            node.left = self._remove(node.left, movieName)
        if node.right:
            node.right = self._remove(node.right, movieName)

        node.setHeight()
        return self.balance(node)

    def top(self, number):
        result = []
        def reverseInorder(n):
            if not n or len(result) >= number:
                return
            reverseInorder(n.right)
            for m in n.movies:
                if len(result) < number:
                    result.append(m)
            reverseInorder(n.left)
        reverseInorder(self.root)
        return result

    def getRatingRange(self, start, end):
        result = []
        def inorder(n):
            if not n:
                return
            if n.movies[0].rating > start:
                inorder(n.left)
            if start <= n.movies[0].rating <= end:
                result.extend(n.movies)
            if n.movies[0].rating < end:
                inorder(n.right)
        inorder(self.root)
        return result
    
    def balance(self, node):
        BF = node.balanceFactor()
        if BF > 1:
            if node.right.balanceFactor() < 0:  
                node.right = node.right.rotateRight()
            node = node.rotateLeft()
        elif BF < -1:
            if node.left.balanceFactor() > 0:
                node.left = node.left.rotateLeft()
            node = node.rotateRight()
        return node

    def getMin(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    
    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def isAVL(self):
        return self._isAVL(self.root)

    def _isAVL(self, node):
        if not node:
            return True
        if abs(node.balanceFactor()) > 1:
            return False
        expected_height = 1 + max(node.left.height if node.left else -1, node.right.height if node.right else -1)
        if node.height != expected_height:
            return False
        return self._isAVL(node.left) and self._isAVL(node.right)
    
    def isBST(self):
        return self._isBST(self.root)

    def _isBST(self, node, min=float('-inf'), max=float('inf')):
        if not node:
            return True
        if not (min <= node.movies[0].rating <= max):
            return False
        return (self._isBST(node.left, min, node.movies[0].rating) and
                self._isBST(node.right, node.movies[0].rating, max))

class Node:
    def __init__(self, movie):
        self.movies = [movie]  
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self):
        return ', '.join(str(m) for m in self.movies)
    
    def balanceFactor(self):
        left_height = self.left.height if self.left else -1
        right_height = self.right.height if self.right else -1
        return right_height - left_height

    def setHeight(self):
        a = self.left.height if self.left else -1
        b = self.right.height if self.right else -1
        self.height = 1 + max(a, b)

    def rotateRight(self):
        new_root = self.left
        self.left = new_root.right
        new_root.right = self
        self.setHeight()
        new_root.setHeight()
        return new_root
    
    def rotateLeft(self):
        new_root = self.right
        self.right = new_root.left
        new_root.left = self
        self.setHeight()
        new_root.setHeight()
        return new_root
    
class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = float(rating)

    def __str__(self):
        return f'{self.title}({self.rating})'


rottenPotato = AVLTree()
movies = [
    ("Megalodon", 5.0),
    ("Inception", 9.1),
    ("The_Dark_Knight", 8.9),
    ("Interstellar", 9.4),
    ("Tenet", 7.2),
    ("Memento", 7.9),
    ("Dunkirk", 7.7),
    ("The_Prestige", 8.3),
    ("Avatar", 7.8),
    ("Titanic", 8.1),
    ("Gladiator", 8.6),
    ("The_Matrix", 9.3),
    ("John_Wick", 7.5),
    ("Parasite", 9.0),
    ("Whiplash", 8.5),
    ("La_La_Land", 8.0),
    ("The_Godfather", 9.2),
    ("Pulp_Fiction", 8.4),
    ("Fight_Club", 8.7),
    ("Forrest_Gump", 8.8)
]

for movie in movies:
    rottenPotato.insertMovie(movie)

inp = input("The Requests From User: ").split(", ")
for request in inp:
    req = request.split(" ")
    if req[0] == "I":
        rottenPotato.insertMovie([req[1], float(req[2])])
    elif req[0] == "D":
        rottenPotato.removeMovie(req[1])
    elif req[0] == "T":
        print(f"Top {req[1]}")
        print([str(movie) for movie in rottenPotato.top(int(req[1]))])
        print()
    elif req[0] == "R":
        print(f'Rating range from {req[1]} to {req[2]}')
        print([str(movie) for movie in rottenPotato.getRatingRange(float(req[1]), float(req[2]))])
        print()
print(f'Is this AVL Tree? {rottenPotato.isAVL() and rottenPotato.isBST()}')