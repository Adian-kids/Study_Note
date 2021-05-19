class Node(object):
    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next = None


class DoubleLinkList(object):
    def __init__(self):
        """初始化双向链表"""
        self.head = None

    def is_empty(self):
        return self.head is None

    def length(self):
        """返回链表长度"""
        if self.is_empty():
            return 0
        else:
            cur = self.head
            count = 0
            while cur != None:
                count += 1
                cur = cur.next
            return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return "[None Object]"
        else:
            cur = self.head
            while cur != None:
                print(cur.item, end=" ")
                cur = cur.next
        print()

    def add(self, item):
        """在链表头部添加结点"""
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def append(self, item):
        """在链表尾部增加结点"""
        node = Node(item)
        if self.is_empty():
            self.head = node
        cur = self.head
        while cur != None:
            if cur.next == None:
                break
            cur = cur.next
        cur.next = node
        node.prev = cur

    def insert(self, pos, item):
        """在指定位置插入结点"""
        node = Node(item)
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            cur = self.head
            for i in range(pos - 1):
                cur = cur.next
            node.next = cur.next
            node.prev = cur
            cur.next.prev = node
            cur.next = node

    def remove(self, item):
        """删除指定结点"""
        if self.is_empty():
            return "[None Object]"
        cur = self.head
        while cur != None:
            if cur.item == item:
                if cur is self.head:
                    self.head = cur.next
                else:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
            cur = cur.next

    def search(self, item):
        """寻找结点是否存在"""
        if self.is_empty():
            return "[None Object]"
        cur = self.head
        count = 0
        while cur != None:
            if cur.item != item:
                cur = cur.next
                count += 1
            else:
                return count
