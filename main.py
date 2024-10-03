from components.filters.color_inversion import ColorInversionFilter
from components.filters.contrast import ContrastFilter
from components.filters.gaussian_blur import GaussianBlurFilter
from components.filters.mirror import MirrorFilter
from components.pipes.last_value import LastValuePipe
from components.sinks.show import ImShowSink
from components.sources.video_capture import VideoCaptureSource
from executor import Executor


def main():
    video_capture = VideoCaptureSource()

    render_queues = [LastValuePipe() for _ in range(2)]

    input_video_show = ImShowSink(
        render_queue=render_queues[0], window_name="Input Video Stream"
    )
    output_video_show = ImShowSink(
        render_queue=render_queues[1], window_name="Output Video Stream"
    )

    video_capture_to_input_video_show = LastValuePipe()
    video_capture.add_output_pipe(video_capture_to_input_video_show)
    input_video_show.set_input_pipe(video_capture_to_input_video_show)

    filters = [
        MirrorFilter(),
        ColorInversionFilter(),
        ContrastFilter(),
        GaussianBlurFilter(),
    ]

    video_capture_to_filters = LastValuePipe()
    video_capture.add_output_pipe(video_capture_to_filters)
    filters[0].set_input_pipe(video_capture_to_filters)

    filter_pipes = [LastValuePipe() for _ in range(len(filters) - 1)]

    for i in range(len(filters) - 1):
        filters[i].add_output_pipe(filter_pipes[i])
        filters[i + 1].set_input_pipe(filter_pipes[i])

    filters_to_output_video_show = LastValuePipe()
    filters[-1].add_output_pipe(filters_to_output_video_show)
    output_video_show.set_input_pipe(filters_to_output_video_show)

    executor = Executor(
        processors=[video_capture, input_video_show, output_video_show, *filters],
        render_queues=render_queues,
    )

    executor.start()


if __name__ == "__main__":
    main()
