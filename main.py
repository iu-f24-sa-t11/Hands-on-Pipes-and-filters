import cv2
from multiprocessing import Queue
from filters import CannyEdge, Mirror, Resize, Save

if __name__ == '__main__':
    sink = Queue()

    save = Save(outputs=[])
    canny_edge = CannyEdge(outputs=[save.input, sink])
    resize = Resize(outputs=[canny_edge.input])
    mirror = Mirror(outputs=[canny_edge.input])

    filters = [
        mirror,
        canny_edge,
        resize,
        save,
    ]

    for f in filters:
        f.start()

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video.")
    else:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            mirror.input.put(frame)

            if not sink.empty():
                processed_frame = sink.get()
                cv2.imshow('Processed Video Stream', processed_frame)

            cv2.imshow('Input Stream', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    for f in filters:
        f.terminate()

    cap.release()
    cv2.destroyAllWindows()
