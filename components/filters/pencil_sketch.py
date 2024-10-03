import cv2

from components.filters import Filter


class PencilSketchFilter(Filter):
    def handle_data(self, data):
        gray = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
        inverted = cv2.bitwise_not(gray)
        blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
        inverted_blurred = cv2.bitwise_not(blurred)
        return cv2.divide(gray, inverted_blurred, scale=256.0)
