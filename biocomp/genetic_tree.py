class TreeNode:
    def __init__(self, data=None, length=0):
        self.children = []
        self.data = data
        self.length = length

    def __str__(self):
        if self.data is None:
            return '(' + ','.join(str(x) for x in self.children) + ')'
        else:
            return self.data

    def add_child(self, node):
        self.children.append(node)

    def add_children(self, node_list):
        for node in node_list:
            self.add_child(node)

    def set_length(self, length):
        self.length = length


def main():
    root = TreeNode()

    aux = TreeNode()
    aux.add_child(TreeNode('A'))
    aux.add_child(TreeNode('C'))
    aux.add_child(TreeNode('E'))

    root.add_child(TreeNode('B'))
    root.add_child(aux)
    root.add_child(TreeNode('D'))

    print(root)


if __name__ == '__main__':
    main()
