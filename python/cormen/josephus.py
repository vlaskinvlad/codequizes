class Node(object):
    def __init__(self, value):
        self.next = None
        self.is_head = False
        self.value = value

class LList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            node.next = node
            node.is_head = True

        else:
            p  = self.tail
            self.tail = node
            p.next = node
            node.next = self.head
        self.size += 1

    def insert_int(self, i):
        n = Node(i)
        self.insert(n)

    def remove_int(self, i):
        current = self.head
        z = 0
        while current.value != i and z<= size:
            current = current.next
            z+= 1

if __name__ ==
