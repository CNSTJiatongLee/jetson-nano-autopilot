from .zmq_camera import ZmqCamera
from .opencv_gst_camera import OpenCvGstCamera
from .image import bgr8_to_jpeg

try:
    DEFAULT_CAMERA = os.environ['JETBOT_DEFAULT_CAMERA']
except:
    DEFAULT_CAMERA = 'opencv_gst_camera'


if DEFAULT_CAMERA == 'zmq_camera':
    Camera = ZmqCamera
else:
    Camera = OpenCvGstCamera