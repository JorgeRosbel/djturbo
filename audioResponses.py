import sounddevice as sd
import numpy as np
from pedalboard import Pedalboard, Reverb, Gain, Delay, HighpassFilter, LowpassFilter, PitchShift #love them
import librosa

stream = None
y = None
sr = None
current_gesture = None
current_volume = 0.8
blocksize = 1024
y_ptr = 0

#a tunear:
boards = {
    "spread": Pedalboard([Gain(gain_db=6)]),
    "pinch":  Pedalboard([Gain(gain_db=-10)]),
    "ok":     Pedalboard([HighpassFilter(cutoff_frequency_hz=3000)]),
    "bad":    Pedalboard([LowpassFilter(cutoff_frequency_hz=1000)]),
    "fist":   Pedalboard([Gain(gain_db=-100)]),
    "great":  Pedalboard([PitchShift(semitones=7)]),
}

def audio_callback(outdata, frames, time, status):
    global y_ptr
    block = y[y_ptr:y_ptr + frames]
    if len(block) < frames:
        block = np.pad(block, (0, frames - len(block)))

    if current_gesture in boards:
        block = boards[current_gesture](block, sr)

    block = block * current_volume

    outdata[:] = block.reshape(-1, 1)
    y_ptr = (y_ptr + frames) % len(y)

def process_gesture(gesture: str):
    global current_gesture
    if gesture != current_gesture:
        print(f"🎛 Cambio de gesto: {current_gesture} → {gesture}")
    current_gesture = gesture

def set_volume(volume: float):
    global current_volume
    current_volume = max(0.0, min(1.0, float(volume)))

def start_audio(audio_path: str):
    global stream, y, sr
    y, sr = librosa.load(audio_path, sr=None)
    stream = sd.OutputStream(callback=audio_callback, samplerate=sr, channels=1, blocksize=blocksize)
    stream.start()