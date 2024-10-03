# Hands-on-Pipes-and-filters

## Codebase organisation:

Hands-on-Pipes-and-filters/
├── filter/
│   ├── __init__.py       // Exposes the Filter class and the override decorator
│   ├── decorator.py      // Contains decorators for image filtering functions
│   └── filter.py         // Manages filter application and image processing logic
├── filters/
│   ├── __init__.py       // Imports all filters for simplified access in the filters package
│   ├── canny_edge.py     // Implements the Canny edge detection filter
│   ├── mirror.py         // Implements the image mirroring (flipping) filter
│   ├── resize.py         // Implements the image resizing filter
│   └── save.py           // Handles saving processed images
├── README.md             // Project description, setup instructions, and usage examples
├── main.py               // Main script that runs the project and applies filters
└── requirements.txt      // Specifies project dependencies, including the required OpenCV version

### Hands-on-Pipes-and-filters/filter/decorator.py:
TODO

### Hands-on-Pipes-and-filters/filter/filter.py:
This module includes the Filter abstract base class, which is used to handle the lifespan of a filter operation via Python's multiprocessing module. The class enables filters to execute in parallel processes and requires that any subclass implement the run() function to describe filter logic. The class also includes methods for starting and terminating the filter process, resulting in an organized approach to filter management.

### Hands-on-Pipes-and-filters/filters/canny_edge.py:
This module defines the CannyEdge filter, which uses the Canny edge detection technique on input frames. It derives from the Filter class and processes frames with the cv2.Canny() function. The frames are routed through a multiprocessing queue, and the edge-detected frames are distributed to several outputs. The run method continues to process frames until it receives a termination signal.

### Hands-on-Pipes-and-filters/filters/mirror.py:
The Mirror filter in this module flips input frames horizontally (mirroring them) using Opencv cv2.flip() method. The class is derived from Filter and processes frames using a multiprocessing queue, sending mirrored frames to many outputs. Like the other filters, it processes frames indefinitely until it gets a termination signal.

### Hands-on-Pipes-and-filters/filters/resize.py:
This module defines the Resize filter, which uses OpenCV's cv2.resize() method to reduce the size of input frames by half. The class inherits from the Filter base class and processes frames concurrently. The resized frames are routed to numerous outputs via a multiprocessing queue, and the run procedure repeats until it is terminated.

### Hands-on-Pipes-and-filters/filters/save.py:
The Save filter in this module saves the input frames to disk as image files using OpenCV's cv2.imwrite() method. It is derived from Filter and manages frames that pass through a multiprocessing queue, saving each frame and routing it to several outputs. The filter operates constantly until it gets a termination signal, at which time it ceases processing frames.

### Hands-on-Pipes-and-filters/main.py:
This is the application's main entry point; it collects video from a camera, applies a number of image filters, and shows both the input and processed video streams in real time. Core functionality includes:
- Video Capture: The script captures video from the camera using OpenCV (cv2.VideoCapture(0)).
- Filters Setup: The script creates four filters (Mirror, Resize, CannyEdge, and Save) that are used to process video frames in a pipeline.
- Multiprocessing: Each filter is executed in a distinct process using Python's multiprocessing package. Frames are transmitted between filters using queues.
- Display: The processed frames appear in a window alongside the original input stream. When you press the 'q' key, the software terminates and all filter processes are stopped.
