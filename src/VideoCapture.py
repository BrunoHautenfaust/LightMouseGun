import cv2
from threading import Thread

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
        self.stopped = False
        (self.grabbed, self.frame) = self.stream.read()
        Thread(target=self.__get, args=()).start()
        return self


    def stop(self):
        self.stopped = True
        if self.stream is not None:
            self.stream.release()

    def __get(self):
        while not self.stopped:
            if not self.grabbed:
                self.stop()
            else:
                (self.grabbed, self.frame) = self.stream.read()
