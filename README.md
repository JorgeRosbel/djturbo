# DJ Turbo — Hand Gesture Music Mixer

▶︎ •၊၊||၊|။||||။‌‌‌‌‌၊|၊၊၊၊||၊|။||||။‌‌‌‌‌၊|||၊|။||||။‌‌‌‌‌၊၊၊||၊|။||||။‌‌‌‌‌၊|၊၊||၊|။||||။‌‌‌‌‌၊||•
```
 ________         ___          _________    ___  ___      ________      ________      ________
|\   ___ \       |\  \        |\___   ___\ |\  \|\  \    |\   __  \    |\   __  \    |\   __  \
\ \  \_|\ \      \ \  \       \|___ \  \_| \ \  \\\  \   \ \  \|\  \   \ \  \|\ /_   \ \  \|\  \
 \ \  \ \\ \   __ \ \  \           \ \  \   \ \  \\\  \   \ \   _  _\   \ \   __  \   \ \  \\\  \
  \ \  \_\\ \ |\  \\_\  \           \ \  \   \ \  \\\  \   \ \  \\  \|   \ \  \|\  \   \ \  \\\  \
   \ \_______\\ \________\           \ \__\   \ \_______\   \ \__\\ _\    \ \_______\   \ \_______\
    \|_______| \|________|            \|__|    \|_______|    \|__|\|__|    \|_______|    \|_______|
```

Control music effects and volume live with just your hands — no controllers, no knobs.

## Requirements

- Python 3.10+
- Webcam
- Audio output device
- Any MP3 file (bring your own)

## Installation

```bash
git clone https://github.com/belubeluga/dj-turbo.git
cd dj-turbo
python -m venv myVenv
source myVenv/bin/activate  # Windows: myVenv\Scripts\activate
pip install -r requirements.txt
```

## Running

```bash
python main.py path/to/your/song.mp3
```

## How It Works

DJ Turbo uses your webcam and MediaPipe to track both hands in real time. Each hand has a distinct role:

### Effects Hand (left side of screen by default — your right hand)

Make a gesture to apply an audio effect:

| Gesture | How to do it | Effect |
|---|---|---|
|✊ |FIST	|MUTE
|🖐 |SPREAD	|GAIN +6dB
|🤏 |PINCH	|GAIN −10dB
|👌 |GREAT	|PITCH +12 SEMITONES
|👍 |OK	|HIGHPASS 3kHz
|👎 |BAD	|LOWPASS 1kHz

### Volume Hand (right side of screen by default — your left hand)

Open your palm (spread), then **rotate your wrist** VOLUME 0 → 100%
Keep any other gesture and the volume stays locked at the last level.

### Keyboard Controls

| Key | Action |
|---|---|
| `s` | Swap which hand controls effects vs volume |
| `q` | Quit |

The current hand assignment is always shown in the window.

## License

MIT — see [LICENSE](LICENSE).

```
████████████████████████████████████████
████████████████████████████████████████
██████▀░░░░░░░░▀████████▀▀░░░░░░░▀██████
████▀░░░░░░░░░░░░▀████▀░░░░░░░░░░░░▀████
██▀░░░░░░░░░░░░░░░░▀▀░░░░░░░░░░░░░░░░▀██
██░░░░░░░░░░░░░░░░░░░▄▄░░░░░░░░░░░░░░░██
██░░░░░░░░░░░░░░░░░░█░█░░░░░░░░░░░░░░░██
██░░░░░░░░░░░░░░░░░▄▀░█░░░░░░░░░░░░░░░██
██░░░░░░░░░░████▄▄▄▀░░▀▀▀▀▄░░░░░░░░░░░██
██▄░░░░░░░░░████░░░░░░░░░░█░░░░░░░░░░▄██
████▄░░░░░░░████░░░░░░░░░░█░░░░░░░░▄████
██████▄░░░░░████▄▄▄░░░░░░░█░░░░░░▄██████
████████▄░░░▀▀▀▀░░░▀▀▀▀▀▀▀░░░░░▄████████
██████████▄░░░░░░░░░░░░░░░░░░▄██████████
████████████▄░░░░░░░░░░░░░░▄████████████
██████████████▄░░░░░░░░░░▄██████████████
████████████████▄░░░░░░▄████████████████
██████████████████▄▄▄▄██████████████████
████████████████████████████████████████
████████████████████████████████████████
```
