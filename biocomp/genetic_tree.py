class TreeNode:
    def __init__(self, data=None, length=None):
        self.children = []
        self.data = data
        self.length = length

    def add_child(self, node):
        self.children.append(node)

    def add_children(self, node_list):
        for node in node_list:
            self.add_child(node)

    def set_length(self, length):
        self.length = length

    def __str__(self):
        length_str = ''
        if self.length is not None:
            length_str = ':' + str(round(self.length, 4))

        if self.data is None:
            return '(' + ','.join(str(x) for x in self.children) + ')' + length_str
        else:
            return self.data + length_str


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
