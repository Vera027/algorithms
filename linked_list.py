class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def print_list(self):
        llist = self.head
        while llist is not None:
            print(llist.value)
            llist = llist.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.tail
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    def prepend(self, value):
        node1 = Node(value)
        if self.length == 0:
            self.head = node1
            self.tail = node1
        else:
            node1.next = self.head
            self.head = node1
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = value

    def insert(self, index, value):
        temp = self.get(index - 1)
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend()
        elif index == self.length - 1:
            return self.append()
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        prev = self.get(index - 1)
        if index < 0 or index > self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


my_linked_list = LinkedList(1)
# append 2 for the linked list and print the linked list
my_linked_list.append(2)
my_linked_list.print_list()

# pop the last item from linked list
print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())

# prepend 3 and print the linked list
my_linked_list.prepend(3)
my_linked_list.prepend(5)
my_linked_list.print_list()

# run pop_first from the linked list
print(my_linked_list.pop_first)
print(my_linked_list.set_value(1, 2))

# insert value 3 at position 2
my_linked_list.append(1)
my_linked_list.append(9)
my_linked_list.append(2)
my_linked_list.insert(2, 3)
my_linked_list.print_list()

# remove value whose index is 2
my_linked_list.remove(2)
my_linked_list.print_list()


# reverse the linked list
my_linked_list.reverse()
my_linked_list.print_list()

