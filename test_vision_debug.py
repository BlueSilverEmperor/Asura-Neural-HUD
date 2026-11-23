import sys
import os

try:
    print("Attempting direct import of solutions...")
    import mediapipe.python.solutions as solutions
    print("Success: import mediapipe.python.solutions works")
    print(f"Solutions dir: {dir(solutions)}")
except ImportError as e:
    print(f"Direct import failed: {e}")

try:
    print("\nAttempting import via mediapipe...")
    import mediapipe as mp
    if hasattr(mp, 'solutions'):
        print("mp.solutions exists")
    else:
        print("mp.solutions does NOT exist")
        # specific check for python 3.13 issue
        try:
             import mediapipe.python.solutions as mp_solutions
             mp.solutions = mp_solutions
             print("Monkey-patching mp.solutions successful")
        except:
             print("Monkey-patching failed")

except Exception as e:
    print(f"General Error: {e}")
