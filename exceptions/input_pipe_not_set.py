class InputPipeNotSet(Exception):
    def __init__(self):
        super().__init__("Input pipe not set. Use the set_input_pipe method to set it.")
