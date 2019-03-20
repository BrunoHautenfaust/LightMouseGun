import cv2
from threading import Thread
import os

class VideoCapture:

    def __init__(self):
        self.stream = None
        self.stopped = False

    def prepare_camera(self, src=0):
        self.stream = cv2.VideoCapture(src)

    def cam_is_available(self):
        if self.stream is None or not self.stream.isOpened():
            return False
        else:
            return True

    def start(self):
        os.system('v4l2-ctl --set-ctrl exposure_auto_priority=0')
        self.stopped = False
        (self.grabbed, self.frame) = self.stream.read()
        Thread(target=self.__get, args=()).start()
        return self


    def stop(self):
        os.system('v4l2-ctl --set-ctrl exposure_auto_priority=1')
        self.stopped = True
        if self.stream is not None:
            self.stream.release()

    def __get(self):
        while not self.stopped:
            if not self.grabbed:
                self.stop()
            else:
                (self.grabbed, self.frame) = self.stream.read()
