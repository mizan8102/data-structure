class Node:
    def __init__(self, dataval=None):
        self.prev = None
        self.next = None
        self.val = dataval


class LinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    # add element in list
    def add(self, val):
        node = Node(val)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1

    def __remove_node(self, node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

    def remove(self, value):
        node = self.head
        while node is not None:
            if node.val == value:
                self.__remove_node(node)
            node = node.next

    def __str__(self):
        vals = []
        node = self.head
        while node is not None:
            vals.append(node.val)
            node = node.next
        return f"[{', '.join(str(val) for val in vals)}]"


my_list = LinkedList()
my_list.add(4)
my_list.add(4)
my_list.add(4)
my_list.add(4)
my_list.add(37)
my_list.add(37)
my_list.add(7)

print(my_list)
my_list.remove(4)
print(f'array={my_list}')
print(f'List size ={my_list.size}')
