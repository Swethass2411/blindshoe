from ultralytics import YOLO
import cv2
import asyncio
import edge_tts
import pygame
import time
import os

# Load trained YOLO model
model = YOLO("runs/detect/train-5/weights/best.pt")

# Initialize pygame
pygame.mixer.init()

last_object = ""
last_time = 0

# Voice function
async def speak(text):
    communicate = edge_tts.Communicate(
        f"{text} detected. {text} detected. {text} detected.",
        "en-US-JennyNeural"
    )

    await communicate.save("voice.mp3")

    pygame.mixer.music.load("voice.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

    pygame.mixer.music.unload()

    if os.path.exists("voice.mp3"):
        os.remove("voice.mp3")


# Open webcam
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Detect objects
    results = model(frame)

    annotated = results[0].plot()

    # If at least one object detected
    if len(results[0].boxes) > 0:

        cls = int(results[0].boxes[0].cls[0])

        object_name = model.names[cls]

        print("Detected:", object_name)

        # Speak once every 3 seconds
        if object_name != last_object or (time.time() - last_time) > 3:

            asyncio.run(speak(object_name))

            last_object = object_name
            last_time = time.time()

    cv2.imshow("YOLO Voice Detection", annotated)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()