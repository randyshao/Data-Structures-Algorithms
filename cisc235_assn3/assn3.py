# Name: Randy Shao
# Student Number: 20100992

class Node:
    # instance variables
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

class Tree:
    def __init__(self):
        self.root = None
        self.count = 0

    def search(self, x):
        node = self.root
        while node is not None:
            if node.value == x:
                return node.value
            elif node.value > x:
                node = node.leftChild
            else:
                node = node.rightChild
        return None

    def searchPath(self, x, pathArray):
        node = self.root
        while node is not None:
            if node.value == x:
                pathArray.append(node.value)
                return pathArray
            elif node.value > x:
                pathArray.append(node.value)
                node = node.leftChild
            else:
                pathArray.append(node.value)
                node = node.rightChild
        return None

    def insert(self, x):
        self.count += 1
        self.root = self.recInsert(self.root, x)

    def recInsert(self, node, x):
        if node is None:
            self.root = Node(x)
            return self.root
        elif node.value >= x:
            node.leftChild = self.recInsert(node.leftChild, x)
        else:
            node.rightChild = self.recInsert(node.rightChild, x)
        return node

    def delete(self, x):
        self.root = self.recDelete(self.root, x)

    def recDelete(self, node, x):
        if node is None:
            return node
        else:
            if node.value < x:
                node.rightChild = self.recDelete(node.rightChild, x)
                return node
            elif node.value > x:
                node.leftChild = self.recDelete(node.leftChild, x)
                return node
            else:
                if node.leftChild is None:
                    return node.rightChild
                elif node.rightChild is None:
                    return node.leftChild
                else:
                    tmp = self.fix_left_subtree(node)
                    tmp.rightChild = node.rightChild
                    return tmp

    def fix_left_subtree(self, v):
        temp = v.leftChild  # temp is the root of v’s

    # left subtree
        if temp.rightChild is None:
            return temp  # no fix needed
        else:
            parent = None
            node = temp
            while node.rightChild is not None:
                parent = node
                node = node.rightChild
            parent.rightChild = node.leftChild
            node.leftChild = temp
            return node

    def averageDepth(self):
        total = self.calcDepth(self.root, [], 1)
        count = 0
        for i in total:
            count += i
        return count / self.count

    def calcDepth(self, node, avgDepth, counter):

        if node is None:
            return 0
        else:
            self.calcDepth(node.leftChild, avgDepth, counter + 1)
            avgDepth.append(counter)
            self.calcDepth(node.rightChild, avgDepth, counter + 1)
        return avgDepth

    def maxDepth(self, node):
        if node is None:
            return 0
        leftDepth = self.maxDepth(node.leftChild)
        rightDepth = self.maxDepth(node.rightChild)

        if leftDepth > rightDepth:
            return leftDepth + 1
        else:
            return rightDepth + 1

    def preOrder(self, x):
        if x is None:
            return
        else:
            print(x.value)
            self.preOrder(x.leftChild)
            self.preOrder(x.rightChild)

if __name__ == "__main__":
    bst = Tree()
    nodeArray = [6, 3, 17, 8, 20, 7, 12, 10]
    for node in nodeArray:
        bst.insert(node)
    print("Binary Search Tree Values: ")
    bst.preOrder(bst.root)
    for node in nodeArray:
        print("Search value: ", bst.search(node))
    for node in nodeArray:
        print("Search Path: ", bst.searchPath(node, []))
    print("Average Depth: ", bst.averageDepth())
    print("Max Depth: ", bst.maxDepth(bst.root))
    bst.delete(17)
    print("Updated Binary Search Tree:")
    bst.preOrder(bst.root)









