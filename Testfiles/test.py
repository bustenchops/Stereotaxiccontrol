class Worker:
    def __init__(self, name):
        self.name = name

    def do_work(self):
        print(f"{self.name} is working.")

class MainClass:
    def __init__(self):
        self.workers = []

    def create_worker(self, name):
        worker = Worker(name)
        self.workers.append(worker)
        print(f"Worker {name} created.")

    def start_all_workers(self):
        for worker in self.workers:
            worker.do_work()

if __name__ == "__main__":
    main = MainClass()
    main.create_worker("Alice")
    main.create_worker("Bob")
    main.start_all_workers()