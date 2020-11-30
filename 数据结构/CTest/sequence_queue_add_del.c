void insert(sequece_queue *sq,datatype x){
	int i;
	if (sq->rear == MAXSIZE)
	{
		printf("\n顺序队列是满的！");
		exit(1);
	}
	sq->a[sq->rear] = x;
	sq->rear = sq->rear + 1;
}

void dele(sequece_queue *sq){
	if (sq->front == sq->rear)
	{
		printf("\n顺序队列是空的！");
		exit(1);
	}
	sq->font++;
}