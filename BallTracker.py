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
    imghsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    imghsv = cv2.GaussianBlur(imghsv, (9, 9), 2)
    imgth = cv2.inRange(imghsv, np.array([20,70,70]), np.array([60,200,200]))
    circles = cv2.HoughCircles(imgth, cv2.HOUGH_GRADIENT, 1.2, 100)
    if circles is not None:
    	# convert the (x, y) coordinates and radius of the circles to integers
    	circles = np.round(circles[0, :]).astype("int")

    	# loop over the (x, y) coordinates and radius of the circles
    	for (x, y, r) in circles:
    		# draw the circle in the output image, then draw a rectangle
    		# corresponding to the center of the circle
    		cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
    		cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
    return frame

if __name__ == '__main__':
    main()
