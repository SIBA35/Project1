from ultralytics import YOLO  # Import YOLO model from ultralytics
import cv2                    # Import OpenCV library
import math                   # Import math module for mathematical operations

# Start webcam
cap = cv2.VideoCapture(0)      # Open default camera (index 0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)   # Set frame width properly
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Set frame height properly

# Load the YOLO model
model = YOLO("yolo-Weights/yolo11n.pt")  # Make sure the path is correct

# List of class names
classNames = [
    "person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat", "traffic light",
    "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow",
    "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee",
    "skis", "snowboard", "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard",
    "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple",
    "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa",
    "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard",
    "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase",
    "scissors", "teddy bear", "hair drier", "toothbrush","box","glass","cap","pen","pencil"
]

# Infinite loop to continuously use the YOLO model on captured frames
while True:
    # Read a frame from the camera
    success, img = cap.read()
    if not success:
        break

    # Perform object detection using YOLO model
    results = model(img, stream=True)

    # Iterate through the result of object detection
    for r in results:
        boxes = r.boxes  # Extract bounding boxes for detected objects
        
        # Iterate through each bounding box
        for box in boxes:
            # Extract coordinates of the bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            # Draw rectangle around detected object
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Extract the class id
            cls = int(box.cls[0])

            # Prepare text label
            label = classNames[cls] if cls < len(classNames) else f"Class {cls}"
            org = (x1, y1 - 10 if y1 - 10 > 10 else y1 + 10)

            # Draw class name
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 0.5
            color = (255, 0, 0)
            thickness = 2
            cv2.putText(img, label, org, font, fontScale, color, thickness)

    # Display the frame with detected objects
    cv2.imshow('Cam', img)

    # Check for 'q' key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
