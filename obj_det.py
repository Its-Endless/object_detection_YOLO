import cv2
import pyttsx3
from ultralytics import YOLO

engine = pyttsx3.init()

def announce_object(object_name, direction, distance):
    engine.say(f"{object_name} detected {direction}, approximately {distance} meters away")
    engine.runAndWait()

def get_direction(x_center, frame_width):
    if x_center < frame_width * 0.33:
        return "on your left"
    elif x_center > frame_width * 0.66:
        return "on your right"
    return "ahead"

def calculate_distance(box_height):
    k = 1000 
    c = 0.5  
    box_height = box_height.item()
    distance = max(k / box_height + c, 0)
    return round(distance, 1)

model = YOLO('yolov5s.pt')

target_objects = {"car", "bus", "bicycle", "person", "motorcycle", "truck"}

cap = cv2.VideoCapture(0)
detected_objects_in_frame = set()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(frame)
    class_names = results[0].names
    predictions = results[0].boxes

    current_frame_objects = set()

    for box in predictions:
        object_class = int(box.cls)
        object_name = class_names[object_class]

        if object_name in target_objects:
            x_center = (box.xyxy[0][0] + box.xyxy[0][2]) / 2
            direction = get_direction(x_center, frame.shape[1])
            box_height = abs(box.xyxy[0][3] - box.xyxy[0][1])
            distance = calculate_distance(box_height)

            current_frame_objects.add((object_name, direction, distance))

    for obj, direction, distance in current_frame_objects:
        if (obj, direction) not in detected_objects_in_frame:
            announce_object(obj, direction, distance)

    detected_objects_in_frame = {(obj, direction) for obj, direction, _ in current_frame_objects}

    annotated_frame = results[0].plot()
    cv2.imshow('YOLO Object Detection', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
