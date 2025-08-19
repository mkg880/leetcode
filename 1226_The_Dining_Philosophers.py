import threading
class DiningPhilosophers:

    def __init__(self):
        self.locks = [threading.Lock() for _ in range(5)]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        right = philosopher
        left = (philosopher + 1) % 5
        if philosopher % 2 == 1:
            left, right = right, left
        with self.locks[right], self.locks[left]:
            pickLeftFork()
            pickRightFork()
            eat()
            putLeftFork()
            putRightFork()
