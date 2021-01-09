class Manager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert "Worker" in [el.__name__ for el in worker.__class__.__mro__], "'worker' must be of type Worker"

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


class Worker:
    def work(self):
        print("I'm working!!")


class SuperWorker(Worker):
    def work(self):
        print("I work very hard!!!")


class LazyWorker(Worker):
    def work(self):
        print("I do not work very hard...")


class Animal:
    def feed(self):
        return "I am eating!"


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
lazy_worker = LazyWorker()
animal = Animal()

try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")
