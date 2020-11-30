void insert(sequence_list *slt,datatype x,int position){
	int i;
	if (slt->size == MAXSIZE)
	{
		printf("\n顺序表是满的！无法插入！");
		exit(1);
	}
	if (position < 0 || position > slt->size)
	{
		printf("\n指定的插入位置不存在！");
		exit(1);
	}
	for (i = slt->size; i > position; i--)
	{
		slt->a[i] = slt->a[i-1];
	}
	slt->a[position] = x;
	slt->size++
}