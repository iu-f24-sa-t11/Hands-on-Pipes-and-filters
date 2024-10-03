# Hands-on-Pipes-and-filters

## Team 11
| Full name       | Group     | Email                           |
|-----------------|-----------|---------------------------------|
| Azamat Bayramov | B22-SD-03 | a.bayramov@innopolis.university |
| Darya Koncheva  | B22-SD-02 | d.koncheva@innopolis.university |
| Matthew Rusakov | B22-SD-03 | m.rusakov@innopolis.university  |
| Egor Valikov    | B22-CBS-01| e.valikov@innopolis.university  |

## Codebase organisation:
<pre>
Hands-on-Pipes-and-Filters/
├── components/
│   ├── filters/
│   │   ├── __init__.py               # Initializes the filters module, making filter classes accessible
│   │   ├── color_inversion.py        # Applies a color inversion filter to a video stream
│   │   ├── contrast.py               # Adjusts the contrast of frames in a video stream
│   │   ├── gaussian_blur.py          # Applies Gaussian blur to video frames for smoothing
│   │   ├── mirror.py                 # Mirrors video frames horizontally
│   │   ├── pencil_sketch.py          # Converts video frames into a pencil sketch effect
│   │   ├── proxy.py                  # Acts as a proxy to manage filters
│   ├── pipes/
│   │   ├── __init__.py               # Initializes the pipes module
│   │   ├── last_value.py             # Holds the last processed value in the pipeline
│   │   ├── queue.py                  # Implements a queue pipe for storing processed frames
│   ├── sinks/
│   │   ├── __init__.py               # Initializes the sinks module
│   │   ├── show.py                   # Displays video frames on the screen or sends them to an output
│   ├── sources/
│   │   ├── __init__.py               # Initializes the sources module
│   │   ├── video_capture.py          # Captures video from a camera or a video file
│   ├── __init__.py                   # Initializes the components module
│   ├── processor.py                  # Handles the processing of video frames through different components
├── exceptions/
│   ├── __init__.py                   # Initializes the exceptions module
│   ├── input_pipe_not_set.py         # Custom exception raised when an input pipe is not configured
├── README.md                         # Documentation on how to set up and run the project
├── __init__.py                       # Root module initialization file
├── executor.py                       # Manages the execution and orchestration of filters, pipes, and sinks
├── main.py                           # Main entry point of the application; initializes components and starts the video processing
├── requirements.txt                  # Lists the necessary dependencies and Python packages to install

</pre>

## Setup Instructions 
To run this application, you should:
1. Clone the Repository
```bash
  git clone https://github.com/iu-f24-sa-t11/Hands-on-Pipes-and-filters.git
  cd Hands-on-Pipes-and-Filters
```
2. Install Dependencies
```bash
  pip install -r requirements.txt
```
3. Connect Your Camera
4. Run the Application
```bash
  python main.py
```

## Link to YouTube video:
TODO
