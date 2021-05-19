def preorder(root):
    """先序遍历"""
    if root == None:
        return "Done"
    print(root.item)
    preorder(root.lchild)
    preorder(root.rchild)

def inorder(root):
    """中序遍历"""
    if root == None:
        return "Done"
    inorder(root.lchild)
    print(root.item)
    inorder(root.rchild)
    
def posorder(root):
    """后续遍历"""
    if root == None:
        return "Done"
    inorder(root.lchild)
    inorder(root.rchild)
    print(root.item)

