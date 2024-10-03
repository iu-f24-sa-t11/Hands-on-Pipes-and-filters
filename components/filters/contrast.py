import cv2

from components.filters import Filter


class ContrastFilter(Filter):
    def __init__(self, alpha=1.25, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.alpha = alpha

    def handle_data(self, data):
        return cv2.convertScaleAbs(data, alpha=self.alpha, beta=0)
