class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleCircleLinkList(object):
    def __init__(self):
        """初始化单向循环链表"""
        self.head = None

    def is_empty(self):
        """判断列表是否为空"""
        return self.head is None

    def length(self):
        """返回单向循环链表的长度"""
        if self.is_empty():
            return 0
        else:
            cur = self.head
            count = 1
            while cur.next != self.head:
                count += 1
                cur = cur.next
            return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return "[No Object]"
        else:
            cur = self.head
            while True:
                print(cur.item, end=" ")
                if cur.next == self.head:
                    break
                cur = cur.next
            print("\n")

    def add(self, item):
        """在头部添加结点"""
        node = Node(item)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = node
            node.next = self.head
            self.head = node

    def append(self, item):
        """在尾部添加结点"""
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = node
            node.next = self.head

    def insert(self, pos, item):
        """在指定位置插入结点"""
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            node = Node(item)
            cur = self.head
            for i in range(pos - 1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """删除指定结点"""
        if self.is_empty():
            return "None Object"
        cur = self.head
        pre = cur
        if cur.item == item:
            while cur.next != self.head:
                cur = cur.next
            cur.next = cur.next.next
        else:
            while cur.next != self.head:
                if cur.item != item:
                    pre = cur
                    cur = cur.next
                else:
                    pre.next = cur.next
                    break

    def search(self, item):
        """查找指定结点是否存在"""
        if self.is_empty():
            return "None Object"
        count = 0
        cur = self.head
        while cur.next != self.head:
            if cur.item != item:
                cur = cur.next
                count += 1
            else:
                return count

