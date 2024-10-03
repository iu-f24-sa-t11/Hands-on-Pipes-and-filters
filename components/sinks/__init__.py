from abc import ABC
from typing import override

from components.pipes import Pipe
from components.processor import Processor


class Sink(Processor, ABC):
    def __init__(self, input_pipe: Pipe | None = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.input_pipe: Pipe | None = input_pipe

    def set_input_pipe(self, input_pipe: Pipe | None):
        self.input_pipe = input_pipe

    @override
    def get_input_data(self):
        return self.input_pipe.get()

    @override
    def handle_data(self, data):
        return data
