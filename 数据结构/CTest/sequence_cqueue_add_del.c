void insert_sequence_cqueue(sequence_queue *sq;datatype x){
    if ((sq->rear + 1) % MAXSIZE == sq->front)
    {
        printf("full");
        exit(1);
    }
    sq->a[sq-rear] = x;
    sq->rear = (sq->rear + 1) % MAXSIZE;
               //和front位置相同就是满
    
}

void dele_sequence_cqueue(sequence_queue *sq){
    if (sq->front == sq->rear)
    {
        printf("empty");
        exit(1);
    }
    sq->front = (sq->front + 1) % MAXSIZE;
}