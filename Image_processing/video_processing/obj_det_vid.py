import cv2

# Function to perform motion detection
def detect_motion(prev_frame, current_frame):
    # Convert frames to grayscale
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    current_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)

    # Compute the absolute difference between frames
    frame_diff = cv2.absdiff(prev_gray, current_gray)

    # Apply thresholding to create a binary image
    _, thresh = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)

    # Find contours of moving objects
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize list to store bounding boxes of detected objects
    bounding_boxes = []

    # Loop over detected contours
    for contour in contours:
        # Get bounding box coordinates and size
        x, y, w, h = cv2.boundingRect(contour)
        
        # Filter out small objects
        if cv2.contourArea(contour) > 1000:
            bounding_boxes.append((x, y, w, h))

    return bounding_boxes

# Main function to perform object tracking
def main():
    # Open a video file or capture from camera
    video_path = 'obj_det_vid.mp4' 
    # Replace with your video file path
    cap = cv2.VideoCapture(video_path)

    # Check if video opened successfully
    if not cap.isOpened():
        print("Error opening video file")
        return

    # Read the first frame
    ret, prev_frame = cap.read()
    if not ret:
        print("Error reading video file")
        return

    while True:
        # Read a new frame
        ret, current_frame = cap.read()
        if not ret:
            break
        
        # Detect motion and get bounding boxes
        bounding_boxes = detect_motion(prev_frame, current_frame)

        # Update previous frame for next iteration
        prev_frame = current_frame.copy()

        # Initialize tracker for each bounding box
        trackers = []
        for bbox in bounding_boxes:
            tracker = cv2.TrackerKCF_create()
            trackers.append(tracker)
            tracker.init(current_frame, bbox)

        # Loop over trackers and update each
        for tracker in trackers:
            success, bbox = tracker.update(current_frame)
            if success:
                # Draw bounding box
                p1 = (int(bbox[0]), int(bbox[1]))
                p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
                cv2.rectangle(current_frame, p1, p2, (0, 255, 0), 2)

        # Display frame with bounding boxes
        cv2.imshow('Object Tracking', current_frame)

        # Exit if ESC pressed
        if cv2.waitKey(1) & 0xFF == 27:
            break

    # Release video capture and close windows
    cap.release()
    cv2.destroyAllWindows()