
class Queue(object):

    def __init__(self):
        self.a = []
        self.b = []

    def enqueue(self, val):
        self.a.append(val)

    def __refill(self):
        if self.a:
            while self.a:
                z = self.a.pop()
                self.b.append(z)

    def dequeue(self):
        if not self.isempty():
            self.__refill()
            return self.b.pop()
        else:
            return None

    def peek(self):
        if not self.isempty():
            self.__refill()
            if self.b:
                return self.b[-1]
            else:
                return None
        else:
            return None

    def isempty(self):
        return len(self.a) == 0 and len(self.b) == 0
