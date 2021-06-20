def breadth(root):
    if root == None:
        return "Done"
    node_list = []
    while node_list:
        node = node_list.pop(0)
        print(node.item)
        if node.lchild != None:
            node_list.append(node.lchild)
        if node.rchild != None:
            node_list.append(node.rchild)
    

