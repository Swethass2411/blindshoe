from ultralytics import YOLO
import cv2
import pyttsx3
import time

# Load trained model
model = YOLO("runs/detect/train-3/weights/best.pt")

# Initialize text-to-speech
engine = pyttsx3.init()
engine.setProperty("rate", 150)

last_spoken = ""
last_time = 0

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    annotated_frame = results[0].plot()

    # Get detected objects
    if len(results[0].boxes) > 0:
        cls = int(results[0].boxes[0].cls[0])
        object_name = model.names[cls]

        # Speak only once every 3 seconds for the same object
        if object_name != last_spoken or time.time() - last_time > 3:
            print("Detected:", object_name)
            engine.say(object_name)
            engine.runAndWait()
            last_spoken = object_name
            last_time = time.time()

    cv2.imshow("YOLO Webcam Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()