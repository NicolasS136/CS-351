from time import sleep
from picamera2 import Picamera2, Preview

camera = Picamera2()
camera_config = camera.create_preview_configuration()
camera.configure(camera_config)
camera.start_preview(Preview.QTGL)
camera.start()
sleep(5)
camera.capture_file("test.jpg")