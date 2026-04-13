import os
import sys
import math
import cv2
import numpy as np
import mediapipe as mp

from funcionesHand import _detect_gesture, _detect_rotation
from audioResponses import process_gesture, set_volume, start_audio

if len(sys.argv) < 2:
    print("Usage: python main.py <path/to/audio.mp3>")
    sys.exit(1)
audio_path = sys.argv[1]

deviceID = 0  # 0 = open default camera

videoCamera = cv2.VideoCapture(deviceID)
if not videoCamera.isOpened():
    print("Error: Could not open video capture device")

start_audio(audio_path)

cv2.namedWindow('Hand Tracking DJ Turbo', cv2.WINDOW_NORMAL)

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=2,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.5
    )

while True:

    retVal, frame = videoCamera.read()
    if not retVal:
        print("Error en videoCamera.read()")
        break

    frame = cv2.flip(frame, 1) #flip horizontal (espejo)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    effects_gesture = None
    volume_display = None

    if results.multi_hand_landmarks:
        h, w, _ = frame.shape
        for hand_landmarks in results.multi_hand_landmarks:

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            wrist = hand_landmarks.landmark[0]
            wrist_px = (int(wrist.x * w), int(wrist.y * h))

            if wrist.x <= 0.5:
                # EFFECTS HAND (left side of screen = user's right hand)
                gesture = _detect_gesture(hand_landmarks)
                if gesture:
                    process_gesture(gesture)
                    effects_gesture = gesture
                cv2.putText(frame, f"FX: {gesture or '-'}",
                            (wrist_px[0] - 40, wrist_px[1] - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            else:
                # VOLUME HAND (right side of screen = user's left hand)
                gesture = _detect_gesture(hand_landmarks)
                if gesture == 'spread':
                    angle = _detect_rotation(hand_landmarks)
                    # Use π/4 half-range (90° total) for very responsive volume control
                    volume = (angle + math.pi / 6) / (2 * math.pi / 6)
                    set_volume(volume)
                    volume_display = f"Vol: {int(max(0.0, min(1.0, volume)) * 100)}%"
                else:
                    volume_display = "Vol: (open hand)"
                cv2.putText(frame, volume_display,
                            (wrist_px[0] - 40, wrist_px[1] - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 180, 0), 2)

    if effects_gesture:
        cv2.putText(frame, f"FX: {effects_gesture}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    if volume_display:
        cv2.putText(frame, volume_display, (10, 65),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 180, 0), 2)
    
    cv2.imshow('Hand Tracking TURBO DJ', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
            
    #time.sleep(0.01)

videoCamera.release()
cv2.destroyAllWindows()


