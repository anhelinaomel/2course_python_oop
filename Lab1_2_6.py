# Create a class BINARY TREE that contains background information of product prices (product code, price of 1 product).
# The tree is sorted by product codes. From the keyboard enter data on the number of products in the format: product code,
# number of products. Using a tree, find the cost of products (cost = quantity * price of one product).

class BTNode:
    def __init__(self, p_code, p_price):
        self.p_code = p_code
        self.p_price = p_price
        self.left = None
        self.right = None
        self.parent = None
 
    def insert(self, node):
        if self.p_code > node.p_code:
            if self.left is None:
                self.left = node
                node.parent = self
            else:
                self.left.insert(node)
        elif self.p_code <= node.p_code:
            if self.right is None:
                self.right = node
                node.parent = self
            else:
                self.right.insert(node)

    def p_code_search(self, p_code, p_amount):
        if self.p_code > p_code:
            if self.left is None:
                print("Product code", p_code, "doesn't exist")
            else:
                self.left.p_code_search(p_code, p_amount)
        elif self.p_code < p_code:
            if self.right is None:
                print("Product code", p_code, "doesn't exist")
            else:
                self.right.p_code_search(p_code, p_amount)
        else:
            print(self.p_price * p_amount)
 
class BTree:
    def __init__(self):
        self.root = None

    def p_code_search(self, p_code, p_amount):
        if self.root is not None:
            self.root.p_code_search(p_code, p_amount)

    def add(self, p_code, p_price):
        new_node = BTNode(p_code, p_price)
        if self.root is None:
            self.root = new_node
        else:
            self.root.insert(new_node)

btree = BTree()

btree.add(349821, 34.99)
btree.add(234200, 9.59)
btree.add(904036, 2.99)
btree.add(955832, 0.89)
btree.add(324189, 45.0)

p_code, p_amount = input("Enter product code and amount:").split()
btree.p_code_search(int(p_code), int(p_amount))
