# Object Detection with YOLO 🚀
[![Python](https://img.shields.io/badge/Python-3.8-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)  
[![OpenCV](https://img.shields.io/badge/OpenCV-4.5.3-5C3C6B.svg?style=flat&logo=OpenCV)](https://opencv.org)  
[![YOLO](https://img.shields.io/badge/YOLO-4.0-FF4F00.svg?style=flat&logo=YOLO)](https://github.com/ultralytics/yolov5)  

This project demonstrates **Object Detection with YOLO** to assist visually impaired individuals. It uses real-time detection to identify and announce detected objects along with their spatial directions (e.g., "Car detected on your left, approximately 5 meters away").

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration Options](#configuration-options)
- [Troubleshooting](#troubleshooting)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview

This **Object Detection with YOLO** project helps visually impaired individuals by detecting objects in the environment and announcing them through an audio system. It uses the YOLO (You Only Look Once) model for real-time object detection and **pyttsx3** for text-to-speech functionality. The system also estimates the distance of detected objects and announces their approximate distance along with their spatial direction (left, right, or ahead).

## Features
- **Real-time Object Detection:** Using YOLO to detect objects in a live camera feed.
- **Audio Announcements:** Announcements for detected objects with spatial directions (left, right, ahead).
- **Customizable Object Detection:** Pre-configured to detect various objects like cars, people, and trucks.
- **Distance Estimation:** Estimates the distance of detected objects using bounding box height.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Its-Endless/object_detection_YOLO.git
   ```

2. Navigate to the project directory:
   ```bash
   cd object_detection_YOLO
   ```

3. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Launch the script to start object detection:
   ```bash
   python object_detection.py
   ```

5. Press **"q"** to exit the program.

## Usage

- Run the Python script `object_detection.py` to start real-time object detection.
- The system will detect objects like `cars, buses, bicycles, people, motorcycles, and trucks`.
- Detected objects will be announced with their spatial direction (left, right, ahead) and    
  approximate distance in meters.
- Modify the `target_objects` set in the script to customize which objects you want to detect.

## Configuration Options
You can modify the **target objects** that the system will detect by updating the `target_objects` set in the script:
```python
target_objects = {"car", "bus", "bicycle", "person", "motorcycle", "truck"}
```
You can also adjust the distance estimation formula in the `calculate_distance` function:
```python
def calculate_distance(box_height):
    k = 1000  # Scaling factor
    c = 0.5   # Constant offset
    distance = max(k / box_height + c, 0)
    return round(distance, 1)
```

## Troubleshooting

1. **No Sound Output:** Ensure your system audio is enabled, and `pyttsx3` is working correctly.
2. **Camera Not Detected:** Check your webcam or external camera connection.
3. **Library Errors:** Ensure all required libraries are installed using:
   ```bash
   pip install -r requirements.txt
   ```
4. **Distance Estimation Issues:** Adjust the `k` and `c` values in the `calculate_distance` 
   function for better accuracy.
## Technologies Used
- **Python** 3.8
- **OpenCV** (for video capture and frame processing)
- **pyttsx3** (for text-to-speech)
- **YOLOv5** (You Only Look Once for object detection)

## Contributing

Contributions are welcome! Please fork this repository, create a branch, and submit a pull request with your changes. Ensure you follow the existing code style and add tests for any new features.

## License 
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

## Contact
For any questions or inquiries, please reach out to Shubhang Gupta at [shubhgupta916@gmail.com](mailto:your-shubhgupta916@gmail.com).

<a href="#top">Back to top</a>
