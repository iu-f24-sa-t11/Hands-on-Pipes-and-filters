import cv2

from components.filters import Filter


class GaussianBlurFilter(Filter):
    def __init__(self, ksize=(25, 25), sigma=10, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ksize = ksize
        self.sigma = sigma

    def handle_data(self, data):
        return cv2.GaussianBlur(data, self.ksize, self.sigma)
