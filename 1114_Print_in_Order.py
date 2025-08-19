import threading
class Foo:
    def __init__(self):
        self.b = threading.Lock()
        self.c = threading.Lock()
        self.b.acquire()
        self.c.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.b.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        self.b.acquire()
        printSecond()
        self.c.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        self.c.acquire()
        printThird()