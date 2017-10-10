from cv2 import VideoCapture,imwrite

class camera:
    def __init__(self):
        self.camera_port = 0

        self.ramp_frames = 15
        self.camera = VideoCapture(self.camera_port)

    def get_image(self):
        self.retval, self.im = self.camera.read()
        return self.im

    def capture(self,filename):

        for i in xrange(self.ramp_frames):
            self.temp = self.get_image()
        print("Taking image...")

        self.camera_capture = self.get_image()
        self.file = filename

        imwrite(self.file, self.camera_capture)

        del (self.camera)