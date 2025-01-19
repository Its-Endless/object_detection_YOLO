# Object Detection with YOLO 🚀
This project demonstrates object detection using the YOLO model to help visually impaired individuals. It includes real-time detection and announces detected objects with their spatial directions (e.g., "Car detected on your left").

# Features
• Real-time object detection using the YOLO model.
• Audio announcements for detected objects with direction.
• Pre-configured to detect objects like cars, bicycles, persons, etc.

# Prerequisites
Before running the project, make sure you have the following installed:
1. Python 3.8 or higher
2. pip (Python package manager)

# Libraries Required
Install the following Python libraries:

1. OpenCV (for video capture and frame processing)
   ```sh
   pip install opencv-python
   ```
2. pyttsx3 (for text-to-speech)
   ```sh
   pip install pyttsx3
   ```
3. Ultralytics YOLO (for YOLO model):
   ```sh
   pip install ultralytics
   ```
# How to Run the Project

1. Clone the Repository
   ```sh
   git clone https://github.com/Its-Endless/object_detection_YOLO.git
   cd object_detection_YOLO
   ```
2. Set Up the Environment
   If you use a virtual environment, set it up using the following commands:
   ```sh
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```
3. Install the Dependencies
   Run the following command to install all required libraries:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Script
   Execute the script to start object detection:
   ```sh
   python object_detection.py
   ```
5. Exit the Program
   Press "q" to exit the program during real-time detection.

# Configuration Options

• Modify Target Objects
  You can adjust the target_objects set in the script to detect specific objects:
  ```sh
  target_objects = {"car", "bus", "bicycle", "person", "motorcycle", "truck"}
  ```
# Troubleshooting

1. No Sound Output: Ensure your system audio is enabled, and pyttsx3 is configured correctly.
2. Camera Not Detected: Verify your webcam or external camera connection.
3. Library Errors: Ensure all required libraries are installed using pip install.

# Contributions

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

# License

This project is licensed under the MIT License.
