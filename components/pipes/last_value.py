from components.pipes import Pipe


class LastValuePipe(Pipe):
    def __init__(self):
        self.value = None

    def put(self, data):
        self.value = data

    def get(self):
        return self.value
