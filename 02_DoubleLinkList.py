# coding:utf-8

class Node(object):
    '''结点'''
    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None

class DoubleLinkList(object):
    '''双链表'''
    def __init__(self, node=Node):
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
        '''
        方法一：
            先新元素的后继结点指向头结点
            再头指针指向新元素，此时新元素已经变为链表的头结点
            最后新元素的下一结点的前驱结点指向新元素
        '''
        node.next = self.__head
        self.__head = node
        node.next.prev = node
        '''方法二：
            先新元素的后继结点指向头结点
            再头结点的前驱结点指向新元素
            最后头指针指向新元素
            node.next = self.__head
            self.__head.prev = node
            self.__head = node
        '''

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
            node.prev = cur

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
            cur = self.__head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
            # 当循环退出后，cur指向pos位置
            node = Node(item)
            # 方法一：
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node
            '''
            方法二：
            node.next = cur
            node.prev = cur.prev
            cur.prev = node
            node.prev.next = node
            '''

    def remove(self, item):
        '''删除结点'''
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                # 先判断此结点是否是头结点
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        # 判断链表是否只有一个结点
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        # 判断删除的元素是否是尾结点
                        cur.next.prev = cur.prev
                break
            else:
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
    dll = DoubleLinkList()
    print(dll.is_empty())
    print(dll.length())

    dll.append(1)
    print(dll.is_empty())
    print(dll.length())

    dll.append(2)
    dll.add(8)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.append(6)
    dll.travel()         # 8 1 2 3 4 5 6
    dll.insert(-1, 9)    # 9 8 1 2 3 4 5 6
    dll.travel()
    dll.insert(3, 100)   # 9 8 1 100 2 3 4 5 6
    dll.travel()
    dll.insert(10, 200)  # 9 8 1 100 2 3 4 5 6 200
    dll.travel()
    dll.remove(100)  # 9 8 1 2 3 4 5 6 200
    dll.travel()
    dll.remove(9)  # 8 1 2 3 4 5 6 200
    dll.travel()
    dll.remove(200)  # 8 1 2 3 4 5 6
    dll.travel()