import cv2
import numpy as np
import time
video_file = ""

def pixel_to_ascii(pixel_intensity)-> str:
    ASCII_CHARS = "@%#*+=-. "
    s = ASCII_CHARS[int(pixel_intensity * len(ASCII_CHARS) / 256)]
    return s

#the zero in videocapture stand for webcam but you can put your video file variable
capture = cv2.VideoCapture(0) #capture the video from local file

#get frames per second for video

fps = capture.get(cv2.CAP_PROP_FPS)


#frames duration per millisecond

frame_duration_ms = int(1000/fps)


width = 150

height = 50
count = 0
success = 1

frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
height = int((width*frame_height/frame_width)*0.4194)
#arr= []
while success:
    success,image = capture.read()
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #cv2.imwrite("frame%d.jpg" %count,gray)
    count+=1
    #resize the image
    resize = cv2.resize(gray,(width,height),interpolation=cv2.INTER_LINEAR)
    ascii_frames = ""
    for y in range(height):
        
        for x in range(width):
            pixel_value = resize[y, x]
            ascii_frames+=pixel_to_ascii(resize[y,x])
        ascii_frames+="\n"
    print("\033[2J")
    print(ascii_frames)
    time.sleep(frame_duration_ms /1000)

capture.release()

    
    
