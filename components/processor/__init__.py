from abc import ABC, abstractmethod
from threading import Thread


class Processor(ABC):
    def __init__(self):
        self.is_running = False

    def start(self):
        self.is_running = True

        thread = Thread(target=self.run)
        thread.start()

        return thread

    def stop(self):
        self.is_running = False

    def run(self):
        while self.is_running:
            self.process()

    def process(self):
        data = self.get_input_data()

        if data is None:
            return

        handled_data = self.handle_data(data)

        self.put_output_data(handled_data)

    @abstractmethod
    def get_input_data(self):
        pass

    @abstractmethod
    def put_output_data(self, data):
        pass

    @abstractmethod
    def handle_data(self, data):
        pass
