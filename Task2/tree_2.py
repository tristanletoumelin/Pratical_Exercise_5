class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class BinarySearchTree:
    def __init__(self, node_list):
        """ Initialize BinarySearchTree with a list of nodes"""
        self.root = Node(node_list[0])  # Set the first node as the root
        for data in node_list[1:]:
            self.insert(data)  # Insert the remaining nodes into the tree

    def search(self, node, parent, data):
        """ Recursive function to search for a node with a given data value"""
        if node is None:
            return False, node, parent  # Return False if the node is not found
        if node.data > data:
            return self.search(node.lchild, node, data)
        else:
            return self.search(node.rchild, node, data)

    def insert(self, data):
        """ Insert a new node with the given data into the tree"""
        flag, n, p = self.search(self.root, self.root, data)  # Search for the position to insert
        if not flag:
            new_node = Node(data)
            if data > p.data:
                p.rchild = new_node
            else:
                p.lchild = new_node

    def delete(self, root, data):
        """ Delete a node with the given data from the tree"""
        flag, n, p = self.search(root, root, data)  # Search for the node to delete
        if not flag:
            print("No key value found")
        else:
            # Cases for deletion based on the number of children
            if n.lchild is None:
                if n == p.lchild:
                    p.lchild = n.rchild
                else:
                    p.rchild = n.rchild
                del n
            elif n.rchild is None:
                if n == p.lchild:
                    p.lchild = n.lchild
                else:
                    p.rchild = n.lchild
                del n
            else:
                # Node has two children, find the predecessor
                pre = n
                next = n.rchild
                if next.lchild is None:
                    n.data = next.data
                    n.rchild = next.rchild
                    del next
                else:
                    while next.lchild is not None:
                        pre = next
                        next = next.lchild
                    n.data = next.data
                    pre.lchild = next.rchild
                    del next

    def preorder(self, node):
        """ Perform a preorder traversal of the tree and print node values"""
        if node is not None:
            print(node.data)
            self.preorder(node.lchild)
            self.preorder(node.rchild)

    def inorder(self, node):
        """ Perform a postorder traversal of the tree and print node values"""
        if node is not None:
            self.postorder(node.lchild)
            print(node.data)
            self.postorder(node.rchild)

    def postorder(self, node):
        """ Perform a postorder traversal of the tree and print node values"""
        if node is not None:
            self.postorder(node.lchild)
            self.postorder(node.rchild)
            print(node.data)

    def display_tree(self, node, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.data))
            if node.lchild is not None or node.rchild is not None:
                if node.lchild is not None:
                    self.display_tree(node.lchild, level + 1, "L--- ")
                if node.rchild is not None:
                    self.display_tree(node.rchild, level + 1, "R--- ")

if __name__ == "__main__":
    a = [49, 38, 65, 97, 60, 76, 13, 27, 5, 1]

    b = [149, 38, 65, 197, 60, 176, 13, 217, 5, 11]

    c = [49, 38, 65, 97, 64, 76, 13, 77, 5, 1, 55, 50, 24]

    bst_a = BinarySearchTree(a)

    # Example 1: Testing the search method
    search_result, node_found, parent_node = bst_a.search(bst_a.root, bst_a.root, 76)
    print(f"Search Result: {search_result}")
    if search_result:
        print(f"Node Found: {node_found.data}")
        print(f"Parent Node: {parent_node.data}")
    else:
        print("Node not found.")

    # Example 2: Testing the insert method
    bst_a.insert(30)
    print("\nAfter Inserting 30:")
    bst_a.preorder(bst_a.root)

    # Example 3: Testing the delete method
    bst_a.delete(bst_a.root, 38)
    print("\nAfter Deleting 38:")
    bst_a.preorder(bst_a.root)

    # bst_a = BinarySearchTree(a)
    # bst_a.display_tree(bst_a.root)

    # bst_b = BinarySearchTree(b)
    # bst_b.display_tree(bst_b.root)

    # bst_c = BinarySearchTree(c)
    # bst_c.display_tree(bst_c.root)