# Extract image from video file

# conda install opencv
import cv2

# OpenCV: Couldn't read video stream from file "problem_1_surveillance.mp4"
video = cv2.VideoCapture('problem_1_surveillance.mp4')

i = 1
while True:
    ret, image = video.read()

    if not ret:
        break

    cv2.imwrite('Frames/image' + str(i) + '.jpg', image)

    i += 1

video.release()
