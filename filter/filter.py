from abc import ABC, abstractmethod
from multiprocessing import Process


class Filter(ABC):
    def __init__(self, filter_instance):
        self.filter_instance = filter_instance
        self.process = Process(target=self.filter_instance.run)

    def start(self):
        self.process.start()

    def terminate(self):
        self.filter_instance.input.put(None)
        self.process.join()

    @abstractmethod
    def run(self):
        pass
