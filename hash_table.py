"""
methods to solve collisions:
1. separate chaining
2. linear probing

Division method:
h(K) = k mod M
where k is the key value and M is size of the hash table
"""


class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for item in range(len(self.data_map[index])):
                if self.data_map[index][item][0] == key:
                    return self.data_map[index][item][1]
        else:
            return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys


my_hash_table = HashTable()

my_hash_table.set_item('washer', 1300)
my_hash_table.set_item('bolts', 700)
my_hash_table.set_item('lumber', 30)
my_hash_table.print()

print('test get_item')
print(my_hash_table.get_item('washer'))
print(my_hash_table.get_item('abc'))

print('test keys')
print(my_hash_table.keys())


# check if elements in two lists are same(using hash table)
def items_are_same(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True

    for j in list2:
        if j in my_dict:
            return True
    return False


list1 = [1, 2, 5, 7]
list2 = [0, 4, 6, 7]
print(items_are_same(list1, list2))
