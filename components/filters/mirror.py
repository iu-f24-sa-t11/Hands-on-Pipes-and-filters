import cv2

from components.filters import Filter


class MirrorFilter(Filter):
    def handle_data(self, data):
        return cv2.flip(data, 1)
