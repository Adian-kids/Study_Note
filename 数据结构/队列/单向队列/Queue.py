class Queue(object):
    """队列"""
    def __init__(self):
        self.queue_list = []

    def is_empty(self):
        """判断队列是否为空"""
        return self.queue_list == []

    def enqueue(self,item):
        """进队列"""
        self.queue_list.insert(0,item)

    def dequeue(self):
        """出队列"""
        self.queue_list.pop()

    def size(self):
        return len(self.queue_list)
