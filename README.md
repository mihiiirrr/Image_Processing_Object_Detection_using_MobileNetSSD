Project Title: Object Detection using OpenCV and MobileNetSSD

Overview:
This project demonstrates a complete pipeline of computer vision applications using OpenCV and the pre-trained MobileNetSSD deep learning model. It covers fundamental image operations, user interaction through mouse events, thresholding techniques, working with live video streams, motion detection, and advanced object detection on both images and videos. The goal is to gradually build up knowledge from basics of OpenCV to real-time intelligent applications.

Why this project:
This project provides a hands-on understanding of computer vision concepts, starting from fundamentals and building up to advanced deep learning-based object detection. It simulates real-world use cases such as motion-based surveillance, automated object recognition, and interactive image applications. The step-by-step progression of files ensures a solid foundation in both classical computer vision and modern deep learning approaches.


Requirements:

* Python 3.x
* OpenCV (cv2)
* NumPy
* Matplotlib (for visualization in experiments)
* Pretrained MobileNetSSD model files:
  1. MobileNetSSD\_deploy.prototxt (model architecture)
  2. MobileNetSSD\_deploy.caffemodel (pre-trained weights)

Both model files must be downloaded and stored in the specified directory path used in the scripts.

Project Files and Explanations:

1. opencv1.py

   * Reads an image from disk and displays it using both OpenCV and matplotlib.
   * Purpose: First step in understanding OpenCV’s image handling.

2. filter1\_gaussian\_blur.py

   * Applies Gaussian blur to smooth the image while preserving edges better than average blur.
   * Purpose: Reduces noise and detail in images for preprocessing.

3. filter2\_medianblur.py

   * Applies median blur, particularly effective for removing salt-and-pepper noise.
   * Purpose: Provides noise reduction while preserving edges.

4. filter3\_sobel.py

   * Uses the Sobel operator to calculate gradients in horizontal and vertical directions.
   * Purpose: Detects edges and highlights object boundaries in an image.

5. histogram\_equalization.py

   * Enhances the contrast of grayscale images using histogram equalization.
   * Purpose: Makes image features more visible, useful in low-contrast situations.

6. thresholding.py

   * Converts a grayscale image into binary form using fixed thresholding.
   * Purpose: Segments the image into foreground and background for further analysis.

7. segmentation.py

   * Uses Canny edge detection and contour finding to segment objects in an image.
   * Purpose: Identifies and highlights distinct objects or regions within the image.

8. morphological\_trans.py

   * Applies dilation, erosion, and morphological gradient operations on an image.
   * Purpose: Improves shape-based analysis, useful in removing noise or highlighting boundaries.

9. fourier\_transform.py

   * Applies 2D Fourier transform to analyze frequency components of an image.
   * Purpose: Useful in image filtering, noise reduction, and frequency domain analysis.

10. Vid\_pro1.py

    * Captures frames from webcam, converts them to grayscale, saves them into an AVI video file, and displays them live.
    * Purpose: Introduces video recording and processing simultaneously.

11. Vid\_pro2.py

    * Opens webcam, prints default resolution, changes capture dimensions to 960x540, and streams in grayscale.
    * Purpose: Demonstrates controlling camera properties.

12. Vid\_pro3.py

    * Captures video and overlays timestamp and resolution info on each frame.
    * Purpose: Demonstrates annotating live video feeds with metadata.

13. tkinter1.py

    * Creates a GUI with Tkinter to open and display an image with OpenCV.
    * Purpose: Introduces GUI-based image handling.

14. tkinter2.py

    * Tkinter app with buttons to open live video capture and save recorded video.
    * Purpose: Integrates GUI with real-time video capture and recording.

15. tkinter3.py

    * Tkinter app that lets users choose an image and display it inside the GUI using PIL and ImageTk.
    * Purpose: Demonstrates OpenCV and Tkinter integration for user-friendly apps.

16. image\_pro1.py

    * Performs basic geometric transformations such as resizing, flipping, and rotating an image.
    * Purpose: Covers essential image manipulations.

17. image\_pro2.py

    * Adjusts brightness and contrast of images.
    * Purpose: Teaches intensity transformations.

18. image\_pro3.py

    * Performs image addition and blending.
    * Purpose: Shows how multiple images can be combined or enhanced.

19. mouse\_event1.py

    * Left click prints/display coordinates, right click prints/display BGR values on an image.
    * Purpose: Teaches pixel-level operations and user interaction.

20. mouse\_event2.py

    * On left click, draws red circles and connects points with yellow lines on a blank canvas.
    * Purpose: Demonstrates drawing and tracking using mouse events.

21. mouse\_event3.py

    * On left click, retrieves pixel color from image and opens a new window filled with that color.
    * Purpose: Demonstrates pixel access and dynamic image creation.

22. obj\_det\_vid.py

    * Detects motion by comparing consecutive frames, applying thresholding, and finding contours.
    * Purpose: Introduces motion-based object detection.

23. OBJECT\_DETECTION.py

    * Performs object detection on a static image using MobileNetSSD.
    * Purpose: Demonstrates deep learning-based detection on images.

24. VIDEO\_DETECTION.py

    * Applies MobileNetSSD for real-time object detection via webcam.
    * Purpose: Extends object detection to live video streams.

25. prac1.py

    * Similar to OBJECT\_DETECTION but uses an extended class list for testing.
    * Purpose: Practice script to test extended labels and detection.

Model Files Explanation:

* MobileNetSSD\_deploy.prototxt: Defines the network architecture, including all layers, configurations, and connections.
* MobileNetSSD\_deploy.caffemodel: Contains the pre-trained weights of the MobileNetSSD model trained on the Pascal VOC dataset.

Project Flow (Learning Sequence):

1. Start with opencv1.py to understand basic image reading and visualization.
2. Learn thresholding and preprocessing with filter1\_gaussian\_blur.py, filter2\_medianblur.py, filter3\_sobel.py, histogram\_equalization.py, thresholding.py, segmentation.py, morphological\_trans.py, and fourier\_transform.py.
3. Practice live video capture with Vid\_pro1.py, Vid\_pro2.py, and Vid\_pro3.py.
4. Learn user interaction with mouse\_event1.py, mouse\_event2.py, and mouse\_event3.py.
5. Explore basic image processing in image\_pro1.py to image\_pro3.py.
6. Explore GUIs with tkinter1.py, tkinter2.py, and tkinter3.py.
7. Study motion detection with obj\_det\_vid.py.
8. Apply deep learning-based detection with OBJECT\_DETECTION.py on static images.
9. Extend to real-time video detection with VIDEO\_DETECTION.py.
10. Use prac1.py for testing and practicing with additional datasets and labels.


How to Run:

1. Ensure Python, OpenCV, and NumPy are installed.
2. Place the MobileNetSSD model files (prototxt and caffemodel) in the correct directory.
3. Update image/video file paths in the scripts as needed.
4. Run scripts individually using: python filename.py
   Example: python OBJECT\_DETECTION.py
5. For live video detection, run VIDEO\_DETECTION.py and press 'q' to quit.
