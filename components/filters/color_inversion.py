import cv2

from components.filters import Filter


class ColorInversionFilter(Filter):
    def handle_data(self, data):
        return cv2.bitwise_not(data)
