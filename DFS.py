# preOrder
def dfs_pre_order(self):
    result = []

    def traverse1(current_node):
        result.append(current_node.value)
        if current_node.left is not None:
            traverse1(current_node.left)
        if current_node.right is not None:
            traverse1(current_node.right)

    traverse1(self.root)
    return result


# postOrder
def dfs_post_order(self):
    results = []

    def traverse2(current_node):
        if current_node.left is not None:
            traverse2(current_node.left)
        if current_node.right is not None:
            traverse2(current_node.right)
        results.append(current_node.value)

    traverse2(self.root)
    return results


# InOrder
def dfs_in_order(self):
    result1 = []

    def traverse3(current_node):
        if current_node.left is not None:
            traverse3(current_node.left)
        result1.append(current_node.value)
        if current_node.right is not None:
            traverse3(current_node.right)

    traverse3(self.root)
    return result1



