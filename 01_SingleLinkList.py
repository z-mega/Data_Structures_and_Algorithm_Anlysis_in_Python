# coding:utf-8

class Node(object):
    '''结点'''
    # 构造一个结点的构造函数
    def __init__(self, elem):
        # elem存储数据, next存储指针
        self.elem = elem
        self.next = None

class SingleLinkList(object):
    '''单链表'''
    def __init__(self, node=None):
        # 加2下划线设为私有
        self.__head = None

    def is_empty(self):
        '''链表是否为空'''
        return self.__head == None

    def length(self):
        '''链表长度'''
        # cur游标，用来移动遍历结点
        cur = self.__head
        # count记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历整个链表'''
        cur = self.__head
        while cur != None:
            print(cur.elem, end=' ')
            cur = cur.next
        print('')

    def add(self, item):
        '''链表头部添加元素，头插法'''
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        '''链表尾部添加元素，尾插法'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

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
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                # 先判断此结点是否是头结点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                    # 若用一下代码删除结点可以只用一个游标
                    # pre.next = pre.next.next
                break
            else:
                pre = cur
                cur = cur.next


    def search(self, item):
        '''查找结点是否存在'''
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

# 测试
if __name__ == "__main__":
    sll = SingleLinkList()
    print(sll.is_empty())
    print(sll.length())

    sll.append(1)
    print(sll.is_empty())
    print(sll.length())

    sll.append(2)
    sll.add(8)
    sll.append(3)
    sll.append(4)
    sll.append(5)
    sll.append(6)
    # 8 1 2 3 4 5 6
    sll.insert(-1, 9)   # 9 8 1 2 3 4 5 6
    sll.travel()
    sll.insert(3, 100)  # 9 8 1 100 2 3 4 5 6
    sll.travel()
    sll.insert(10, 200) # 9 8 1 100 2 3 4 5 6 200
    sll.travel()
    sll.remove(100)     # 9 8 1 2 3 4 5 6 200
    sll.travel()
    sll.remove(9)       # 8 1 2 3 4 5 6 200
    sll.travel()
    sll.remove(200)     # 8 1 2 3 4 5 6
    sll.travel()