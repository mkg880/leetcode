import threading
class H2O:
    def __init__(self):
        self.h_sem = threading.Semaphore(2)
        self.o_sem = threading.Semaphore(0)
        self.m = threading.Lock()
        self.h = 0

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        self.h_sem.acquire()
        releaseHydrogen()
        self.m.acquire()
        self.h += 1
        if self.h == 2:
            self.o_sem.release()
            self.h = 0
        self.m.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        # releaseOxygen() outputs "O". Do not change or remove this line.
        self.o_sem.acquire()
        releaseOxygen()
        self.h_sem.release()
        self.h_sem.release()