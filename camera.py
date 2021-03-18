import cv2

cap = cv2.VideoCapture(0)

name = "default_name"
framesTarget = 10
exposure = 0.1
gain = 1

frameWidth = cap.get(CAP_PROP_FRAME_WIDTH)
frameHeight = cap.get(CAP_PROP_FRAME_HEIGHT)

frameNumber = 1

cap.set(CAP_PROP_AUTO_EXPOSURE, 0.25)
cap.set(CAP_PROP_GAIN, gain)
cap.set(CAP_PROP_EXPOSURE, exposure)

while frameNumber <= framesTarget :
  ret, frame = cap.read()
  if frameNumber == 1:
    cv2.imshow('image capture', frame)
  cv2.imwrite(name + str(frameNumber) +".tif", frame)
  frameNumber = frameNumber + 1


while True:
  ret, frame = cap.read()
  
  cv2.imshow('webcam feed' , frame)
  if cv2.waitKey(1) & 0xFF == ord(' '):
    break
    
cap.release()
cv2.destroyAllWindows()