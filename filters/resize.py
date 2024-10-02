import cv2
from multiprocessing import Queue
from filter import Filter, override


class Resize(Filter):
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
            height, width = frame.shape[:2]
            resized_frame = cv2.resize(frame, (width // 2, height // 2))
            for output in self.outputs:
                output.put(resized_frame)
