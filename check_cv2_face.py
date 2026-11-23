import cv2
import sys

print(f"OpenCV Version: {cv2.__version__}")
try:
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    print("SUCCESS: cv2.face.LBPHFaceRecognizer is available.")
except AttributeError:
    print("FAILURE: cv2.face module not found. Need opencv-contrib-python.")
except Exception as e:
    print(f"ERROR: {e}")
