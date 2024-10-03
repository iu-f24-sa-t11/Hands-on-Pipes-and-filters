from abc import ABC
from typing import override

from components.pipes import Pipe
from components.processor import Processor


class Source(Processor, ABC):
    def __init__(self, output_pipes: list[Pipe] | None = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.output_pipes: list[Pipe] = [] if output_pipes is None else output_pipes

    def set_output_pipes(self, output_pipes: list[Pipe]):
        self.output_pipes = output_pipes

    def add_output_pipe(self, output_pipe: Pipe):
        self.output_pipes.append(output_pipe)

    @override
    def handle_data(self, data):
        return data

    @override
    def put_output_data(self, data):
        for output_pipe in self.output_pipes:
            output_pipe.put(data)
