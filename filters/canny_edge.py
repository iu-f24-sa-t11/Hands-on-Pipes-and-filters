import cv2
from multiprocessing import Queue
from filter import Filter, override


class CannyEdge(Filter):
    def __init__(self, outputs):
        super().__init__(self)
        self.outputs = outputs
        self.input = Queue()

    @override
    def run(self):
        while True:
            frame = self.input.get()
            if frame is None:  # Check for termination signal
                break
            edges = cv2.Canny(frame, 100, 200)
            for output in self.outputs:
                output.put(edges)
