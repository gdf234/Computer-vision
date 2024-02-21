import cv2

cap = cv2.VideoCapture("counting.mp4")
ret, frame1 = cap.read()
ret, frame2 = cap.read()

count_line_position = 550

def center_point(x,y,w,h):  # for counting car 
    x1=int(w/2)
    y1=int(h/2)
    cx= x+x1
    cy= y+y1
    return cx,cy

detect = []
offset = 6     # allowable error between pixel
counter = 0

while cap.isOpened():
    add_frame = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(add_frame,cv2.COLOR_BAYER_BG2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(frame1, contours, -1, (0,255,0), 2)
    cv2.line(frame1, (25,count_line_position), (1000,count_line_position), (255,0,0), 2)
    
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) <900:
            continue
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(frame1,"car :"+str(counter), (x,y-20), cv2.FONT_HERSHEY_SIMPLEX, 2, (89,150,0), 5)

        center = center_point(x,y,w,h)
        detect.append(center)
        cv2.circle(frame1, center, 4, (0,0,255), -1)

        for (x,y) in detect:
            if y<(count_line_position+offset):
             counter+=1
            cv2.line(frame1, (25,count_line_position), (1000,count_line_position), (255,0,0), 2, cv2.LINE_4)
            detect.remove((x,y))

            cv2.putText(frame1,"car counting :"+str(counter), (400,60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,150,200), 5)

    cv2.imshow("objects counting",frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey (20) == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
