from components.pipes import Pipe


class QueuePipe(Pipe):
    def __init__(self):
        self.queue = []

    def put(self, data):
        self.queue.append(data)

    def get(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)
