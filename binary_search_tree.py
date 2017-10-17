# Name:        Tyler Davis
# Course:      CPE 202
# Instructor:  Dave Parkinson
# Assignment:  Lab 5
# Term:        Fall 2017


class BinarySearchTree:

    def __init__(self):
        """Creates a new BinarySearchTree with a root as None."""
        """Takes no arguments.
        Returns an empty tree."""
        self.root = None

    def find(self, key):
        """Searches for a certain key in a tree."""
        """Takes an integer representing a key in the tree.
        Returns True if the key is in tree and False otherwise."""
        p = self.root
        while p and p.key != key :
            if key < p.key:
                p = p.left
            else:
                p = p.right
        return p != None

    def insert(self, newkey, data = None):
        """Adds a new key to the tree."""
        """Takes an integer representing a new key to be placed and optional data.
        Returns None and modifies the tree."""
        if self.root is None:			 
            self.root = TreeNode(newkey, data)
        else:
            p = self.root
            if p.key > newkey:
                if not p.left:      
                    p.left = TreeNode(newkey, data, parent=p)
                else:
                    p.left.insert(newkey, data)   
            elif p.key < newkey:
                if not p.right:     
                    p.right = TreeNode(newkey, data, parent=p)
                else:
                    p.right.insert(newkey, data)
            else:
                p.data = data

    def delete(self, key):
        """Deletes a key from the tree."""
        """Takes an integer representing a key in the tree.
        Returns None and takes and modifies the tree."""
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
        """Finds a node with a given key."""
        """Takes an integer representing a key in the tree.
        Returns a node in the tree that contains the given key."""
        p = self.root      
        while p and p.key != key :
            if key < p.key:
                p = p.left
            else:
                p = p.right
        return p

    def print_tree(self):
        """Prints the tree out in order."""
        """Takes no arguments.
        Returns None and outputs the tree."""
        if self.root == None:
            print()
        else:
            self.root.inorder_print_tree()

    def is_empty(self):
        """Determines if the tree is empty."""
        """Takes no arguments.
        Returns True if the tree is empty and False otherwise."""
        return self.root == None


class TreeNode:

    def __init__(self, key, data = None, left = None, right = None, parent = None):
        """Creates a new TreeNode with a key."""
        """Takes a key and other, optional arguments.
        Returns a new TreeNode class."""
        self.key = key
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def insert(self, newkey, data = None):
        """Insert new node with key."""
        """Takes a new key and an optional data.
        Returns None and modifies the nodes in the tree."""
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
        """Finds the next node in order."""
        """Takes no arguments.
        Returns the node witht he next key."""
        current = self.right
        while current.left:
            current = current.left
        return current

    def find_min(self):
        """Finds the smallest key value beginning at a node."""
        """Takes no arguments.
        Returns the smallest key from a node."""
        current = self
        while current.left:
            current = current.left
        return current.key

    def find_max(self):
        """Finds the largest key value beginning at a node."""
        """Takes no arguments.
        Returns the largest key from a node."""
        current = self
        while current.right:
            current = current.right
        return current.key

    def inorder_print_tree(self):
        """Prints all the nodes in a tree in order."""
        """Takes no arguments.
        Returns None and outputs all the nodes in the tree."""
        if self.left:
            self.left.inorder_print_tree()
        self.print_node()
        if self.right:
            self.right.inorder_print_tree()

    def print_levels(self):
        """Prints all the keys in a tree and the level of the key."""
        """Takes no arguments.
        Returns None and outputs the keys and the level of the key."""
        if self.left:
            self.left.print_levels()
        level = self.get_level()
        print("key =", self.key, ", level =", level)
        if self.right:
            self.right.print_levels()

    def get_level(self):
        """Finds the level of a given node."""
        """Takes no arguments.
        Returns an integer representing the level of the key."""
        current = self
        level = 0
        while current.parent:
            current = current.parent
            level += 1
        return level

    def update(self, other):
        """Updates a node with another node's information."""
        """Takes another node as an argument.
        Returns None and updates the node with the data from another node."""
        self.key = other.key
        self.data = other.data
        self.left = other.left
        self.right = other.right
        self.parent = other.parent

    def print_node(self):
        """Prints a node."""
        """Takes no arguments.
        Returns None and outputs all the data of the node."""
        if self.parent:
            print("key =", self.key, ", data =", self.data, ", parent key: ", self.parent.key)
        else:
            print("key =", self.key, ", data =", self.data, ", root")
