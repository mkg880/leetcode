class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        node = self.head
        i = 0
        while i < index:
            if not node:
                return -1
            node = node.next
            i += 1
        if not node:
            return -1
        return node.val

    def addAtHead(self, val: int) -> None:
        self.head = Node(val, self.head)
        if not self.tail:
            self.tail = self.head

    def addAtTail(self, val: int) -> None:
        if not self.tail:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        if not self.head:
            return
        prev = self.head
        i = 1
        while i < index:
            if not prev:
                return
            prev = prev.next
            i += 1
        if not prev:
            return
        prev.next = Node(val, prev.next)
        if self.tail == prev:
            self.tail = prev.next

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        prev = self.head
        i = 1
        while i < index:
            if not prev:
                return
            prev = prev.next
            i += 1
        if not prev or not prev.next:
            return
        if prev.next == self.tail:
            self.tail = prev
        prev.next = prev.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)