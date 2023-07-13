import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale) #This line calculates the new width of the frame by multiplying the original width (frame.shape[1]) with the given scale factor.
    height = int(frame.shape[0] * scale) # This line calculates the new height of the frame by multiplying the original height (frame.shape[0]) with the given scale factor
    dimensions = (width, height) #This line creates a tuple (dimensions) containing the new width and height.
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) #This line resizes the frame using the cv.resize() function from OpenCV. 
    #It takes three parameters: the original frame, the desired dimensions (width and height), and the interpolation method (cv.INTER_AREA in this case, which is suitable for downscaling).

# (OVERALLSUMMARY)=>[Overall, the rescaleFrame function resizes the input frame based on the given scale factor, and returns the resized frame]
capture = cv.VideoCapture('/home/httpstealer/Documents/GitHub/Computer-Vision/CV/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Resized video', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
