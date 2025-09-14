import tkinter as tk
import cv2

class VideoCaptureApp:
    def __init__(self, master):
        self.master = master
        master.title("Video Capture App")

        self.capture_button = tk.Button(master, text="Open Video Capture", bg="yellow",command=self.open_capture)
        self.capture_button.pack(padx=10,pady=20)

        self.write_button = tk.Button(master, text="Write Video", bg="orange",command=self.write_video)
        self.write_button.pack(padx=10,pady=20)

    def open_capture(self):
        cap = cv2.VideoCapture(0)  # Change 0 to the camera index if you have multiple cameras
        while True:
            ret, frame = cap.read()
            cv2.imshow('Video Capture', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

    def write_video(self):
        cap = cv2.VideoCapture(0)  # Change 0 to the camera index if you have multiple cameras
        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

        while True:
            ret, frame = cap.read()
            out.write(frame)
            cv2.imshow('Writing Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release everything if job is finished
        cap.release()
        out.release()
        cv2.destroyAllWindows()

root = tk.Tk()
root.geometry("300x300")
app = VideoCaptureApp(root)
root.mainloop()
