# Real-Time Face Mesh Detection

This project uses Python, OpenCV, and Google's MediaPipe library to perform real-time face mesh detection from a webcam feed. It identifies 468 facial landmarks and overlays a tesselation mesh on the detected faces.

![Face Mesh Demo](https://storage.googleapis.com/mediapipe-assets/face_mesh_1.gif)
*(Image: Google MediaPipe)*

## Features

- Real-time face detection and landmark tracking.
- Overlays a detailed face mesh (tesselation) on the video feed.
- Supports detection of up to 2 faces simultaneously.
- Horizontally flips the video feed for a more natural "mirror" view.

## Requirements

- Python 3.7+
- OpenCV
- MediaPipe

## Installation

1.  **Clone the repository (or download the files):**
    ```bash
    git clone https://github.com/Nolstan/face-detection.git
    cd face-detection
    ```

2.  **Install the required Python packages:**
    ```bash
    pip install opencv-python mediapipe
    ```

## Usage

To run the script, execute the following command in your terminal:

```bash
python main.py
```

A window will appear showing your webcam feed with the face mesh overlay. To stop the application, press the **'q'** key.
