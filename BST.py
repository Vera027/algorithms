class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.height = 0

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                else:
                    temp = temp.left
                return True
            else:
                if temp.right is None:
                    temp.right = new_node
                else:
                    temp = temp.right
                return True

    '''
    if root == None return False
    temp = self.root
    while temp is not None:
    if < left
    elif > right
    else == return True
    return False
    '''

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False


my_tree = BinarySearchTree()
print(my_tree.root)

print('test insert')
my_tree.insert(3)
my_tree.insert(1)
my_tree.insert(4)
print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)

print('test contains')
print(my_tree.contains(1))
print(my_tree.contains(5))

