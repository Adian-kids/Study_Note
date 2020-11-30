//插入
void push(sequence_stack *st,datatype x){
    if (st->top == MAXSIZE)
    {
        printf("\n is Full");
        exit(1);
    }
    st->a[st->top] = x;
    st->top++;
    
}

//删除
void pop(sequence_stack *st){
    if (st->top == 0)
    {
        printf("\nThe sequence stack is empty !");
        exit(1);
    }
    st->top--;
}