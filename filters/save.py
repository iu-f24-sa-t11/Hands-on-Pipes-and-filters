import cv2
from multiprocessing import Queue
from filter import Filter, override


class Save(Filter):
    def __init__(self, outputs):
        super().__init__(self)
        self.outputs = outputs
        self.input = Queue()

    @override
    def run(self):
        while True:
            frame = self.input.get()
            if frame is None:
                break
            cv2.imwrite('output_frame.png', frame)
            for output in self.outputs:
                output.put(frame)
