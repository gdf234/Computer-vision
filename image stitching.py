import cv2

img_paths = ['1.jpg, 2.jpg, 3.jpg']

# initialized a list of images 
imgs = []   

# addition images and scaling down the images,Resize the input images according to your need.  
for i in range (len(img_paths)):
    imgs.append(cv2.imread(img_paths[i]))
    imgs[i] = cv2.resize(imgs[i],(0,0),fx=0.2,fy=0.2)

# showing 3 images
    cv2.imshow('1',imgs[0])
    cv2.imshow('1',imgs[1])
    cv2.imshow('1',imgs[2])

 # images stitching
    stitching = cv2.Stitcher.create()
    (process,output) = stitching.stitch(imgs)

 # check procedure working    
    if stitching != cv2.STITCHER_OK:
        print('stitching not successful')
    else:
        print('panaroma is ready')

 # final result  
        cv2.imshow('final result',output) 
        cv2.waitKey(0)

