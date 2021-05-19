class DoubleEndQueue(object):
    def __init__(self):
        self.queue_list = []

    def add_front(self,item):
        """队列头部入队"""
        self.queue_list.insert(0,item)
    
    def add_rear(self,item):
        """队列尾部入队"""
        self.queue_list.append(item)

    def remove_front(self):
        """队列头部出队"""
        self.queue_list.pop(0)
    
    def remove_rear(self):
        """队列尾部入队"""
        self.queue_list.pop()
    
    def size(self):
        return len(self.queue_list)
