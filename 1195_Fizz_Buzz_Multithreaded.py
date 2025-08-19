import threading
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.fizz_lock = threading.Lock()
        self.buzz_lock = threading.Lock()
        self.fizzbuzz_lock = threading.Lock()
        self.num_lock = threading.Lock()
        self.fizz_lock.acquire()
        self.buzz_lock.acquire()
        self.fizzbuzz_lock.acquire()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(3, self.n+1, 3):
            if i % 5 == 0:
                continue
            self.fizz_lock.acquire()
            printFizz()
            self.num_lock.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(5, self.n+1, 5):
            if i % 3 == 0:
                continue
            self.buzz_lock.acquire()
            printBuzz()
            self.num_lock.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for _ in range(15, self.n+1, 15):
            self.fizzbuzz_lock.acquire()
            printFizzBuzz()
            self.num_lock.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1):
            self.num_lock.acquire()
            if i % 15 == 0:
                self.fizzbuzz_lock.release()
            elif i % 5 == 0:
                self.buzz_lock.release()
            elif i % 3 == 0:
                self.fizz_lock.release()
            else:
                printNumber(i)
                self.num_lock.release()