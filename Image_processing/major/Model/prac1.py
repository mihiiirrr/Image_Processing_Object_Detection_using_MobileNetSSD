import numpy as np 
import cv2

# Path to image and model files
img = "D:/Image_processing/Image_processing/major/12.jpg"
prototxt = "D:/Image_processing/Image_processing/major/Model/MobileNetSSD_deploy.prototxt"
model = "D:/Image_processing/Image_processing/major/Model/MobileNetSSD_deploy.caffemodel"
min_confidence = 0.2

# Correct MobileNetSSD class labels (21 classes)
classes = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

# Assign random colors to each class
np.random.seed(543210)
color = np.random.uniform(0, 255, size=(len(classes), 3))

# Load the model
net = cv2.dnn.readNetFromCaffe(prototxt, model)

# Load input image
img = cv2.imread(img)
heigth, width = img.shape[0], img.shape[1]

# Preprocess image into a blob
blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 0.007, (300, 300), 130)

# Forward pass through the network
net.setInput(blob)
detected_objects = net.forward()

# Loop over detections
for i in range(detected_objects.shape[2]):
    confidence = detected_objects[0][0][i][2]

    if confidence > min_confidence:
        class_index = int(detected_objects[0, 0, i, 1])

        # Scale bounding box back to image size
        upper_left_x = int(detected_objects[0, 0, i, 3] * width)
        upper_left_y = int(detected_objects[0, 0, i, 4] * heigth)
        lower_right_x = int(detected_objects[0, 0, i, 5] * width)
        lower_right_y = int(detected_objects[0, 0, i, 6] * heigth)

        # Draw predictions
        prediction_text = f"{classes[class_index]}: {confidence:.2f}%"
        cv2.rectangle(img, (upper_left_x, upper_left_y),
                      (lower_right_x, lower_right_y), color[class_index], 3)
        cv2.putText(img, prediction_text,
                    (upper_left_x, upper_left_y - 15 if upper_left_y > 30 else upper_left_y + 15),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color[class_index], 2)

# Show final image
cv2.imshow("Object Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
