"""

1. Capture camera image
2. Resize image and show
3. Add information for image
3. Detect the face and draw an rectangle around it

IMPORTANT: If camera fail on MacOS, type "sudo killall VDCAssistant" in the terminal

"""

import cv2
from datetime import datetime
from FaceDetector import FaceDetector


class VideoCapture:
    def __init__(self):
        self.__video = cv2.VideoCapture(0)
        self.__detector = FaceDetector()
        self.__count_frames = 0
        self.__last_second = 0
        self.__total_frames = 0
        self.__is_video_running = False
        self.__numpay_frame = None
        self.__now = None
        self.__face_detector = FaceDetector()

    def read(self):
        """
        Read video, get status and numpay image array.

        :return:
        """
        self.__now = datetime.now()
        self.__is_video_running, self.__numpay_frame = self.__video.read()
        self.__resize_frame()
        self.__count_fps()
        self.__numpay_frame = self.__detector.draw_rectangle_by_array(self.__numpay_frame)
        self.__write_video_info()

    def get_numpay_frame(self):
        return self.__numpay_frame

    def release(self):
        self.__video.release()

    def __resize_frame(self):
        """
        Resize the frame image.

        :return:
        """
        image_width = self.__numpay_frame.shape[0]
        image_height = self.__numpay_frame.shape[1]

        image_new_width = int(image_width / 1.5)
        image_new_height = int(image_height / 1.5)

        self.__numpay_frame = cv2.resize(self.__numpay_frame, (image_new_height, image_new_width))

    def __count_fps(self):
        """
        Calculate video FPS.

        :return:
        """

        if self.__now.second != self.__last_second:
            self.__total_frames = self.__count_frames
            self.__count_frames = 0

        self.__last_second = self.__now.second
        self.__count_frames = self.__count_frames + 1

    def __write_video_info(self):
        """
        Write current time and video FPS capture

        :return:
        """
        font_position_top_left_corner = (20, 50)
        font_face = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.6
        font_color = (255, 255, 255)
        line_type = 2

        cv2.putText(
            self.__numpay_frame,
            self.__now.strftime('%Y/%m/%d %H:%M:%S') + ' - ' + str(self.__total_frames) + 'fps',
            font_position_top_left_corner,
            font_face,
            font_scale,
            font_color,
            line_type
        )