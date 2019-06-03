import cv2
import numpy as np

cap = cv2.VideoCapture('test.mp4')

def main():
    while(cap.isOpened()):
        ret, frame = cap.read()
        frame = BallDetect(frame)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break

def BallDetect(frame):
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.GaussianBlur(grey, grey, (9, 9), 2, 2)
    circles = cv2.HoughCircles(grey, circles, cv2.HOUGH_GRADIENT, 1, grey.rows/8, 200, 100, 0, 0)
    for circle in circles:
        cv2.circle(frame, (circles[0], circles[1]), 3, (0,255,0), -1, 8, 0)
        return frame

if __name__ == '__main__':
    main()
