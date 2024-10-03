import cv2

from components.pipes import Pipe
from components.processor import Processor


class Executor:
    def __init__(
            self,
            processors: list[Processor],
            render_queues: list[Pipe],
    ):
        self.processors = processors
        self.render_queues = render_queues
        self.is_running = True

    def start(self):
        for processor in self.processors:
            processor.start()

        self.run()

    def run(self):
        while self.is_running:
            for queue in self.render_queues:
                f = queue.get()
                if f: f()

            cv2.waitKey(1)

    def stop(self):
        self.is_running = False

        for processor in self.processors:
            processor.stop()
