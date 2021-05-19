class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList(object):
    def __init__(self):
        """初始化单链表"""
        self.head = None

    def is_empty(self):
        """判断单链表是否为空"""
        if self.head == None:
            return True
        else:
            return False
        # return self.head == None

    def travel(self):
        """遍历单链表"""
        cur = self.head
        while cur != None:
            print(cur.item, end=" ")
            cur = cur.next
        print("\n")

    def length(self):
        """获取单链表长度"""
        cur = self.head
        count = 1
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def add(self, item):
        """在链表头部添加新结点"""
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def append(self, item):
        """在链表尾部添加新结点"""
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """在指定位置插入结点"""
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            cur = self.head
            count = 0
            while count < pos - 1:
                cur = cur.next
                count += 1
            node = Node(item)
            node.next = cur.next
            cur.next = node


    def search(self, item):
        """查找指定结点是否存在"""
        cur = self.head
        while cur != None:
            if cur.item == item:
                return True
                break
            else:
                cur = cur.next

    def remove(self, item):
        """删除指定结点"""
        cur = self.head
        pre = cur
        while cur != None:
            if cur.item == item:
                if pre == None:
                    self.head = cur.next
                else:
                    pre.next = cur.next
            pre = cur
            cur = cur.next
