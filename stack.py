class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.bottom = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        temp = self.top
        if self.height == 0:
            return None
        elif self.height == 1:
            return None
        else:
            self.top = self.top.next
            temp.next = None
        self.height -= 1
        return temp


# create a stack
my_stack = Stack(3)
my_stack.print_stack()
print('\n')

print('test push')
my_stack.push(1)
my_stack.push(9)
my_stack.push(7)
my_stack.print_stack()

print('test pop')
my_stack.pop()
my_stack.print_stack()
