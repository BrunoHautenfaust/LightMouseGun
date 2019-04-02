import cv2
import pyautogui

class ROI:
    def __init__(self, pos, mouse=0):
        self.position = pos
        self.mouse = mouse
        self.displayWidth, self.displayHeight = pyautogui.size()
        pyautogui.FAILSAFE = False
        pyautogui.MINIMUM_DURATION = 0
        pyautogui.MINIMUM_SLEEP = 0
        pyautogui.PAUSE = 0

    def process(self, frame):
        frame = self.__mirror_flip(frame)
        frame = self.__crop(frame, self.position)
        gray = self.__convert_image_to_grayscale(frame)
        ret, thresh = self.__threshold(gray)
        contours, hierarchy = self.__find_contours(thresh)
        img = self.__draw_contours(frame, contours)
        cImg = self.__find_moment(thresh, img)

        return cImg

    def __mirror_flip(self, frame):
        return cv2.flip(frame, 1)

    def __crop(self, frame, pos):
        h, w, c = frame.shape

        positions = self.__get_positions(h, w)

        x1 = positions.get(pos)['x1']
        y1 = positions.get(pos)['y1']
        x2 = positions.get(pos)['x2']
        y2 = positions.get(pos)['y2']

        return frame[y1:y2, x1:x2]

    def __convert_image_to_grayscale(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    def __threshold(self, frame):
        return cv2.threshold(frame, 220, 255, cv2.THRESH_BINARY)

    def __find_contours(self, frame):
        return cv2.findContours(frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    def __draw_contours(self, frame, contours):
        return cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)

    def __find_moment(self, frame, image):
        cImage = image
    #    print(cImage.shape)
        coefX, coefY = self.__find_scroll_coefficients(cImage)
        # print(coefX, coefY)
        # calculate moments of binary image
        M = cv2.moments(frame)

        # calculate x,y coordinate of center
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            # put text and highlight the center
            cImage = cv2.circle(image, (cX, cY), 5, (0, 0, 0), -1)

            pyautogui.moveTo(cX * coefX, cY * coefY)
            #pyautogui.moveTo(cX * 6.41314554, cY * 4.8)
            #self.mouse.set(cX, cY)
            #x, y = pyautogui.position()
            # print(pyautogui.position())
       
        return cImage

    def __find_scroll_coefficients(self, frame):
        h, w, c = frame.shape
        coX, coY = self.displayWidth / w, self.displayHeight / h
        return coX, coY

    def __get_positions(self, h, w):
        return {
            'top_left': {
                'x1': 0,
                'y1': 0,
                'x2': int(w / 3),
                'y2': int(h / 3)
            },
            'top_center': {
                'x1': int(w / 3),
                'y1': 0,
                'x2': int(2 * (w / 3)),
                'y2': int(h / 3)
            },
            'top_right': {
                'x1': int(2 * (w / 3)),
                'y1': 0,
                'x2': w,
                'y2': int(h / 3)
            },
            'middle_left': {
                'x1': 0,
                'y1': int(h / 3),
                'x2': int(w / 3),
                'y2': int(2 * (h / 3))
            },
            'middle_center': {
                'x1': int(w / 3),
                'y1': int(h / 3),
                'x2': int(2 * (w / 3)),
                'y2': int(2 * (h / 3))
            },
            'middle_right': {
                'x1': int(2 * (w / 3)),
                'y1': int(h / 3),
                'x2': w,
                'y2': int(2 * (h / 3))
            },
            'bottom_left': {
                'x1': 0,
                'y1': int(2 * (h / 3)),
                'x2': int(w / 3),
                'y2': h
            },
            'bottom_center': {
                'x1': int(w / 3),
                'y1': int(2 * (h / 3)),
                'x2': int(2 * (w / 3)),
                'y2': h
            },
            'bottom_right': {
                'x1': int(2 * (w / 3)),
                'y1': int(2 * (h / 3)),
                'x2': w,
                'y2': h
            }
        }
