//前序

void preorder(bintree t){
	if (t)
	{
		printf("%c\n",t->data);
		preorder(t->lchild);
		preorder(t->rchild);
	}
}

//中序
void inorder(bintree t){
	if (t)
	{
		inorder(t->lchild);
		printf("%c\n",t->data);
		inorder(t->rchild);
	}
}

//后序
void postorder(bintree t){
	if (t)
	{
		postorder(t->lchild);
		postorder(t->rchild);
		printf("%c\n",t->data);
	}
}