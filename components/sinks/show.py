import cv2

from components.pipes import Pipe
from components.sinks import Sink


class ImShowSink(Sink):
    def __init__(
        self, render_queue: Pipe, window_name: str = "Video Stream", *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.render_queue: Pipe = render_queue
        self.window_name: str = window_name

    def put_output_data(self, data):
        def show_image():
            cv2.imshow(self.window_name, data)

        self.render_queue.put(show_image)
