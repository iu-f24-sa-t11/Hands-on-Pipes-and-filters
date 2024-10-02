import cv2
from multiprocessing import Queue
from filter import Filter, override


class Mirror(Filter):
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
            mirrored_frame = cv2.flip(frame, 1)  # Flip horizontally
            for output in self.outputs:
                output.put(mirrored_frame)
