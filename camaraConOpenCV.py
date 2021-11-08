import cv2

def setColor(frame, x, y, r, g, b):
    frame[x, y, 0] = b
    frame[x, y, 1] = g
    frame[x, y, 2] = r



vid = cv2.VideoCapture(0)

ret, frame = vid.read()
frameLast = frame
out = frame

current_time = vid.get(0)
last_time = current_time

while(vid.isOpened()):
    ret, frame = vid.read()

    if(ret== False):
        break

    current_time = vid.get(0)
    # If you want system time then replace above line with the following:
    # current_time = datetime.datetime.now()

    cv2.putText(
        frame,'Current time:' + str((current_time - last_time) / 1000000000), 
        (10, 100), 
        cv2.FONT_HERSHEY_SIMPLEX, 
        1,
        (255,255,255),
        2)

    for x in range(0, frame.shape[0]):
        for y in range(0, frame.shape[1]):            
            out[x, y, 0] = min(abs(frame[x, y, 0] - frameLast[x, y, 0]), 255)

            #if b > 0xDD:
            #    frame[x, y, 0] = 255
            #    frame[x, y, 1] = 255
            #    frame[x, y, 2] = 255
            #else:
            #    frame[x, y, 0] = 0
            #    frame[x, y, 1] = 0
            #    frame[x, y, 2] = 0        


    cv2.imshow('frame', frameLast)

    frameLast = frame
    last_time = current_time

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()

print("Hola")