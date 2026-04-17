# Drowsy Driver Detection System

A real-time driver drowsiness detection system built using Python, OpenCV, and Dlib.  
This project monitors eye activity using facial landmarks and triggers an alarm when signs of drowsiness are detected.

---

## Features

- Real-time eye tracking using webcam  
- Eye Aspect Ratio (EAR) calculation  
- Alarm system when drowsiness is detected  
- Lightweight and efficient  
- Audio alert using pygame  

---

## How It Works

The system uses facial landmark detection to track eye movements.

1. Detect face using Dlib  
2. Extract eye landmarks  
3. Compute Eye Aspect Ratio (EAR)  
4. If EAR drops below threshold for a certain number of frames:
   - Trigger alert  
   - Play alarm sound  

---

## Eye Aspect Ratio Formula

The EAR is calculated using distances between eye landmarks:
EAR = ((||p2 - p6|| + ||p3 - p5||) / (2 * ||p1 - p4||))

- Low EAR → Eyes closed → Drowsy  
- Normal EAR → Eyes open  

---

## Tech Stack

- Python3.9
- OpenCV  
- Dlib  
- Imutils  
- Scipy  
- Pygame  

---

## Project Structure
Drowsy-Driver-Detection/

│── main.py

│── music.wav

│── shape_predictor_68_face_landmarks.dat (NOT INCLUDED)

│── README.md

---

## Important Note (Model File)

The file:
shape_predictor_68_face_landmarks.dat

Cannot be uploaded to GitHub due to its large size.

### After downloading:
1. Extract the `.bz2` file  
2. Place it in the project root directory  

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/drowsy-driver-detection.git
cd drowsy-driver-detection
### 2. Install dependencies
```
### 2. Install dependencies
```bash
pip install opencv-python imutils dlib scipy pygame
```
Note: Installing dlib may require CMake and Visual Studio Build Tools on Windows.

---

### 3. Add required files
- Place shape_predictor_68_face_landmarks.dat in project folder
- Ensure music.wav exists

---

### 4. Run the project
```bash
python main.py
```

---

## Usage
- Enter camera ID (usually 0)
- Sit in front of webcam
- The system will:
  - Track your eyes
  - Trigger alarm if drowsiness is detected
- Press Q to exit.

---

## Configuration
You can tweak these values in the code:
```bash
THRESH = 0.85        # EAR threshold
frame_thresh = 20    # Frames before alert
```

---

## Limitations
- Works best in good lighting
- Requires frontal face visibility
- Not optimized for multiple faces
- Performance depends on webcam quality

---

## Future Improvements
- Mobile app integration
- Night vision support
- Head pose detection
- Deep learning-based fatigue detection
- Dashboard with analytics

---

## License
This project is open-source and available under the MIT License.

---

## Acknowledgements
- Dlib Facial Landmark Detector
- OpenCV Community
