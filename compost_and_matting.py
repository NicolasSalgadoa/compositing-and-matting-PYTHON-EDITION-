"""compositing and matting"""
#python edition ;) also done in c++

import numpy as np
import cv2 as cv

def compost_and_matting(thresh_range, image_path, artifact_path,
                        background_path, result_path):
    
    artifact = cv.imread(artifact_path,cv.IMREAD_COLOR)
    background = cv.imread(background_path, cv.IMREAD_COLOR)
    image = cv.imread(image_path,cv.IMREAD_COLOR)

    #resize background
    height = image.shape[0]; width = image.shape[1]
    dim = [width, height]
    background = cv.resize(background, dim)
    
    artifactB = int(np.average(artifact[:,:,0]))
    artifactG = int(np.average(artifact[:,:,1]))
    artifactR = int(np.average(artifact[:,:,2]))
    
    minB = artifactB - thresh_range; maxB = artifactB + thresh_range
    minG = artifactG - thresh_range; maxG = artifactG + thresh_range
    minR = artifactR - thresh_range; maxR = artifactR + thresh_range
    
    maskB = (image[:,:,0] >= minB) & (image[:,:,0] <= maxB)
    maskG = (image[:,:,1] >= minG) & (image[:,:,1] <= maxG)
    maskR = (image[:,:,2] >= minR) & (image[:,:,2] <= maxR)
    mask = maskB & maskG & maskR

    invimg = np.where(mask, 255, 0).astype("uint8")

    result = cv.add(cv.bitwise_and(background, background
                            ,mask = invimg)
            ,cv.bitwise_and(image, image
                            ,mask = cv.bitwise_not(invimg)))

    cv.imwrite(result_path,result)

"""compost_and_matting(30,r"result\foreground\me.png",r"result\artifacts\my_wall.png"
                    ,r"result\background\nature.png",r"result\res.png")"""
