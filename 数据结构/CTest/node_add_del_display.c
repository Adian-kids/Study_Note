void display(node *head){
	node *p;
	p = head->next;
	if (!p)
	{
		printf("\nempty!");
	}
	else
	{
		while(p){
			printf("%5d\n",p->info);
			p = p->next;
		}
	}
}


node *insert(node *head,datatype x,int i){
	node *p,*q;
	q = find(head,i);
	if (!q)
	{
		printf("\nno this node");
		return head;
	}
	p = (node*)malloc(sizeof(node));
	p->info = x;
	p->next = q->next;
	q->next = p;
	return head;
}

node *dele(node *head,datatype x){
	node *pre = head;
	node *q;
	q = head->next;
	while(q && q->info != x){
		pre = q;  
		q = q->next;
	}
	if (q)
	{
		pre->next = q->next;  //pre指向q的前驱 
		free(q);
	}
}