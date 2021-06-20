class Stack(object):
    """栈"""
    def __init__(self):
        self.stack_list = []

    def is_empty(self):
        """判断是否为空栈"""
        return self.stack_list == []

    def push(self,item):
        """添加元素进入栈顶"""
        self.stack_list.append(item)

    def pop(self):
        """弹出栈顶元素"""
        self.stack_list.pop()

    def peek(self):
        """返回栈顶元素"""
        return self.stack_list[len(self.stack_list) - 1]

    def size(self):
        return len(self.stack_list)



