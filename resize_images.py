import cv2 #importing necessary libraries
import os #importing necessary libraries

def image_resize(source, destination): #function "image_resize" has 2 arguments. it needs the image source and then the destination of the image
    for filename in os.listdir(source): #iterate through the source file path
        f = os.path.join(source, filename) #joining the source file path and the file name /source/filename

        if f.endswith('.png'): #if the file 'f' ends with '.png'
            img = cv2.imread(f) #save the file 'f' in the variable 'img'
            new_size = (850,549) #setting the new size of the image
            resize_img = cv2.resize(img, new_size) #resize the image to a width of 850 pixels and a height of 549 pixels and save it in the variable 'resize_img'
            cv2.imwrite(f + '_new.png', resize_img) #saving the resized image in the source file path with '_new.png' added to the end of the file name

    for f in os.listdir(source): #iterate through the source file path
        if f.endswith('_new.png'): #if the file 'f' ends with '_new.png'
            src_path = os.path.join(source, f) #joining the source file path and the file name /source/filename
            dst_path = os.path.join(destination, f) #joining the source file path and the file name /destination/filename
            os.rename(src_path, dst_path) #renaming the src_path to be the dst_path, essentially putting the files we found in the source and putting then in the destination
    return