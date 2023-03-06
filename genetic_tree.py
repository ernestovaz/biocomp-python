class TreeNode:
    def __init__(self, data=None):
        self.children = []
        self.data = data

    def __str__(self):
        if self.data is None:
            return '(' + ','.join(str(x) for x in self.children) + ')'
        else:
            return self.data

    def add_child(self, node):
        self.children.append(node)


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
