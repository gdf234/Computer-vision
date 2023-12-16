import cv2

# video reading
cap = cv2.VideoCapture(0)
opened = cap.isOpened()

# features
fourcc = cv2.VideoWriter_fourcc(*'MJPG')

height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

# frame per second
fps = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter('jj.sutanu',fourcc,fps,(int(width),int(height)))
print(height)
print("Frame are{}".format(fps))

if(opened):
    while(cap.isOpened()):
        ret, frame = cap.read()
        if (ret == True):
         cv2.imshow('hello',frame)
        out.write(frame)
        if(cv2.waitKey(5000)==27):
            break

        out.release()
        cap.release()
        cv2.destroyAllWindows()
        


