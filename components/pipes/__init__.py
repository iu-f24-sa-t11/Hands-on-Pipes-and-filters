from abc import ABC, abstractmethod


class Pipe(ABC):
    @abstractmethod
    def put(self, data):
        pass

    @abstractmethod
    def get(self):
        pass
