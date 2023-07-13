import cv2 as cv


#==================(reading images)===========================

# image=cv.imread('/home/httpstealer/Desktop/CV/Photos/cat_large.jpg') #imread picture ko read krny k liy istamaal hota hai
# cv.imshow('Cat_large',image) # imshow image ko new window pai show krwanay k liy istamal hota hai
# #imshow takes mainly two parameters one is window_name and another is image.
# cv.waitKey(0) # basically a keyboard binding function. it wait for a specific delay or time in millisecond for a key to be pressed.
# # agr hm es main 0 pass kry toh yeah infinite time k liy wait kry ga 

#==================(reading videos)===========================

# # this is a simple script to read a frams from webcam
# capture=cv.VideoCapture('/home/httpstealer/Desktop/CV/Videos/dog.mp4')
# while True:
#     isTure,frame,= capture.read()
#     cv.imshow('Video',frame)
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# #0xFF is a bitmask used to extract the least significant 8 bits (ASCII value) from the key event
# # >ord('d') returns the Unicode code point of d

# # -->cv2.waitkey(1) returns a 32-bit integer corresponding to the pressed key

# # -->& 0xFF is a bit mask which sets the left 24 bits to zero, because ord() returns a value betwen 0 and 255, since your keyboard only has a limited character set

# # -->Therefore, once the mask is applied, it is then possible to check if it is the corresponding key.
# #        ==(Summary of this code)=>[So, in summary, the code opens a video file, reads and displays its frames in a window, and continues this process until the 'd' key is pressed.]
# capture.release() #Closes video file or capturing device. The 
# cv.destroyAllWindows() #destroy all the windows


#==================(resizing and rescalling)===========================
 
image= cv.imread('/home/httpstealer/Documents/GitHub/Computer-Vision/CV/Photos/cat_large.jpg')
cv.imshow('Cat',image)
def rescaleFrame(frame, scale=0.75):
    width= int(frame.shape[1]*scale)
    height= int(frame.shape[0]*scale)
    dimensions= (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
cv.waitKey(0)