# Name:        Tyler Davis
# Course:      CPE 202
# Instructor:  Dave Parkinson
# Assignment:  Lab 5
# Term:        Fall 2017

# final version for class notes

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def find (self, key):   # iterative find method
        p = self.root      # current node
        while p and p.key != key :
            if key < p.key:
                p = p.left
            else:
                p = p.right
        return p != None

    def insert(self, newkey, data = None):
        if self.root is None:			 # if tree is empty
            self.root = TreeNode(newkey, data)
        else:
            p = self.root
            if p.key > newkey:
                if not p.left:      # no left child from root
                    p.left = TreeNode(newkey, data, parent=p)
                else:
                    p.left.insert(newkey, data)   # call insert of TreeNode on left child
            elif p.key < newkey:
                if not p.right:     # no right child from root
                    p.right = TreeNode(newkey, data, parent=p)
                else:
                    p.right.insert(newkey, data)
            else:
                p.data = data

    def delete(self, key):
        current = self.get_node(key)
        if not current.right and not current.left:
            if current.parent.right == current:
                current.parent.right = None
            else:
                current.parent.left = None
        elif current.right and current.left:
            succ = current.find_successor()
            self.delete(succ.key)
            current.key = succ.key
            current.data = succ.data
        else:
            if current == self.root:
                if current.right:
                    current.update(current.right)
                else:
                    current.update(current.left)
            else:
                if current.right:
                    if current == current.parent.right:
                        current.parent.right = current.right
                    else:
                        current.parent.left = current.right
                    current.right.parent = current.parent
                else:
                    if current == current.parent.left:
                        current.parent.left = current.left
                    else:
                        current.parent.right = current.left
                    current.left.parent = current.parent  
         
    def get_node(self, key):
        p = self.root      # current node
        while p and p.key != key :
            if key < p.key:
                p = p.left
            else:
                p = p.right
        return p

    def print_tree(self):
        if self.root == None:
            print()
        else:
            self.root.inorder_print_tree()

    def is_empty(self):
        return self.root == None


class TreeNode:
    """Tree node: left and right child + data which can be any object"""

    def __init__(self,key,data=None,left=None,right=None,parent=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def insert(self, newkey, data = None):
        """  Insert new node with key, assumes key not present """
        p = self
        done = False
        while not done:
            if newkey < p.key:
                if not p.left:
                    done = True
                else:
                    p = p.left
            elif newkey > p.key:
                if not p.right: 
                    done = True
                else:                        
                    p = p.right
            else:
                done = True
        if newkey < p.key:
            p.left = TreeNode(newkey, data, parent = p)
        elif newkey > p.key:
            p.right = TreeNode(newkey, data, parent = p)
        else:
            p.data = data

    def find_successor(self):
        current = self.right
        while current.left:
            current = current.left
        return current

    def find_min(self):
        current = self
        while current.left:
            current = current.left
        return current.key

    def find_max(self):
        current = self
        while current.right:
            current = current.right
        return current.key

    def inorder_print_tree(self):
        """   Print tree content inorder        """
        if self.left:
            self.left.inorder_print_tree()
        self.print_node()
        if self.right:
            self.right.inorder_print_tree()

    def print_levels(self):
        if self.left:
            self.left.print_levels()
        level = self.get_level()
        print("key =", self.key, ", level =", level)
        if self.right:
            self.right.print_levels()

    def get_level(self):
        current = self
        level = 0
        while current.parent:
            current = current.parent
            level += 1
        return level

    def update(self, other):
        self.key = other.key
        self.data = other.data
        self.left = other.left
        self.right = other.right
        self.parent = other.parent

    def print_node(self):
        """   Print Node information """
        if self.parent:
            print("key =", self.key, ", data =", self.data, ", parent key: ", self.parent.key)
        else:
            print("key =", self.key, ", data =", self.data, ", root")

t = BinarySearchTree()
t.insert(8, 'hello')
t.insert(3, 'dog')
t.insert(10)
t.insert(1)
print ("Tree after inserting 8, 3, 10, 1")
t.root.inorder_print_tree()
t.insert(6)
t.insert(4)
t.insert(7)
t.insert(14)
t.insert(13)
print ("Tree after inserting 6, 4, 7, 14, 13")
t.print_tree()
print("Testing find 14")
print(t.find(14))
print("Testing find 15")
print(t.find(15))
t.root.print_levels()
