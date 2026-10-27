# ThingESP Python Library

Python client for [ThingESP](https://thingesp.siddhesh.me). Control a Raspberry Pi or any Linux machine over WhatsApp.

## Install

```bash
pip install paho-mqtt requests opencv-python
```

Drop `ThingESP.py` next to your script.

## Usage

```python
import ThingESP

thing = ThingESP.Client('username', 'project_name', 'credentials')

def handleResponse(query):
    if query == 'hi':
        return 'Hello, whats up'

thing.setCallback(handleResponse).start()
```

Whatever `handleResponse` returns is sent back as the WhatsApp reply.

## API

| Method | What it does |
|---|---|
| `Client(username, projectName, password)` | Connects to the ThingESP broker |
| `.setCallback(fn)` | Registers your message handler |
| `.start()` | Starts the client loop (runs in a thread) |
| `.device_call(to_number, msg)` | Sends a message from the device, unprompted |
| `.sendImage(path, to_number, msg)` | Uploads and sends an image |

### Sending a webcam snapshot

```python
cam = ThingESP.WebcamVideoStream(src=0).start()

def handleResponse(query):
    if query == 'send image':
        cam.saveImage('img.jpg')
        thing.sendImage('img.jpg', 'your_phone_number', "here's your image!")
        return 'image sent'
```

See `basic_example.py` and `image_send_cam_example.py`.

## License

MIT
