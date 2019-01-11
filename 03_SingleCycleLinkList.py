# coding:utf-8

class Node(object):
    '''结点'''
    # 构造一个结点的构造函数
    def __init__(self, elem):
        # elem存储数据, next存储指针
        self.elem = elem
        self.next = None

class SingleCycleLinkList(object):
    '''单向循环链表'''
    def __init__(self, node=None):
        # 加2下划线设为私有
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        '''链表是否为空'''
        return self.__head == None

    def length(self):
        '''链表长度'''
        if self.is_empty():
            return 0
        # cur游标，用来移动遍历结点
        cur = self.__head
        '''
        if cur is None:
            return 0
        '''
        # count记录数量
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历整个链表'''
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=' ')
            cur = cur.next
        # 退出循环，cur指向尾结点，但尾结点的元素未打印
        print(cur.elem)

    def add(self, item):
        '''链表头部添加元素，头插法'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            # 方法一：先找到尾结点，再插入元素
            while cur.next != self.__head:
                cur = cur.next
            # 退出循环，cur指向尾结点
            node.next = self.__head
            self.__head = node
            cur.next = node  # 等价于cur.next = self.__head
            '''
            方法二：先插入新结点，再处理尾部结点指针
            node.next = self.__head
            self.__head = node
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node.next
            cur.next = node
            '''

    def append(self, item):
        '''链表尾部添加元素，尾插法'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 方法一：
            cur.next = node
            node.next = self.__head
            '''
            方法二：
            node.next = cur.next
            cur.next = node
            '''

    def insert(self, pos, item):
        '''指定位置添加元素
        :param pos 从0开始
        '''
        if pos <= 0:
            # 这里认为要在头部添加元素
            self.add(item)
        elif pos > self.length()-1:
            # 这里认为要在尾部添加元素
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < pos-1:
                count += 1
                pre = pre.next
            # 当循环退出后，pre指向pos-1位置
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        '''删除结点'''
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.elem == item:
                # 先判断此结点是否是头结点
                if cur == self.__head:
                    # 删除头结点
                    # 找尾结点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    # 删除中间结点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # 退出循环，cur指向尾结点
        if cur.elem == item:
            if cur == self.__head:
                # 链表只有一个结点
                self.__head = None
            else:
                pre.next = cur.next
                # pre.next = self.__head

    def search(self, item):
        '''查找结点是否存在'''
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 退出循环，cur指向尾结点
        if cur.elem == item:
            return True
        return False

# 测试
if __name__ == "__main__":
    scll = SingleCycleLinkList()
    print(scll.is_empty())
    print(scll.length())

    scll.append(1)
    print(scll.is_empty())
    print(scll.length())

    scll.append(2)
    scll.add(8)
    scll.append(3)
    scll.append(4)
    scll.append(5)
    scll.append(6)
    # 8 1 2 3 4 5 6
    scll.insert(-1, 9)   # 9 8 1 2 3 4 5 6
    scll.travel()
    scll.insert(3, 100)  # 9 8 1 100 2 3 4 5 6
    scll.travel()
    scll.insert(10, 200) # 9 8 1 100 2 3 4 5 6 200
    scll.travel()
    scll.remove(100)     # 9 8 1 2 3 4 5 6 200
    scll.travel()
    scll.remove(9)       # 8 1 2 3 4 5 6 200
    scll.travel()
    scll.remove(200)     # 8 1 2 3 4 5 6
    scll.travel()
