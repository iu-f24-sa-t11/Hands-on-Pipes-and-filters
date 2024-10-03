import cv2

from components.sources import Source


class VideoCaptureSource(Source):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.video_capture = cv2.VideoCapture(0)

    def get_input_data(self):
        ret, frame = self.video_capture.read()
        if not ret:
            return None

        return frame
