class Node(object):
    def __init__(self, item = -1, lchild = None, rchild = None):
        self.item = item
        self.lchild = lchild
        self.rchild = rchild

class Tree(object):
    def __init__(self,root = None):
        self.root = root

    def add(self,item):
        node = Node(item)
        if self.node == None:
            self.root = node
        else:
            node_list = [self.root]
            while node_list:
                cur = node_list.pop(0)
                if cur.lchild == None:
                    cur.lchild = node
                    return "Done"
                elif cur.rchild == None:
                    cur.rchild = node
                    return "Done"
                else:
                    node_list.append(cur.lchild)
                    node_list.append(cur.rchild)



