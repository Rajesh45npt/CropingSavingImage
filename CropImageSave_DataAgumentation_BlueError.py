

import cv2 as cv
import matplotlib.pyplot as plot
import numpy as np
import os, os.path


# ## Parameters



base_Save_Directory = '/media/rose/Windows/Cropped_Validation'
base_Load_Directory = '/media/rose/Windows/Validation'
save_extension = '.png'


(image_crop_height, image_crop_width) = (224,224)
crop_stride = 224




# ##    Iterate over all folder and Images



valid_image_extensions = [".jpg", ".jpeg"] #specify your vald extensions here
valid_image_extensions = [item.lower() for item in valid_image_extensions]

PhoneModel_number_InProgress = 0;
number_Completed_ImageinModel = 0
for phonemodel in os.listdir(os.path.join(base_Load_Directory)):
    PhoneModel_number_InProgress += 1
    number_Completed_ImageinModel = 0
    for file in os.listdir(os.path.join(base_Load_Directory, phonemodel)):
        number_Completed_ImageinModel += 1
        extension = os.path.splitext(file)[1]
        filename = os.path.splitext(file)[0]
        if extension.lower() not in valid_image_extensions:
            continue
        
        image_file = os.path.join(base_Load_Directory,phonemodel,file)
        
        im = cv.imread(image_file)
        #plot.imshow(im)
        #plot.show()
        (image_original_height, image_original_width) = im.shape[0:2]
        
        number_croppedimages_in_width = (image_original_width-image_crop_width)//crop_stride + 1
        number_croppedimages_in_height = (image_original_height-image_crop_height)//crop_stride + 1
        print(filename, number_croppedimages_in_height,number_croppedimages_in_width, PhoneModel_number_InProgress, number_Completed_ImageinModel)
        #input()
        
        
        for count_height in range(number_croppedimages_in_height):
            for count_width in range(number_croppedimages_in_width):
                cropped_image = im[count_height*crop_stride:(count_height*crop_stride + image_crop_height), count_width*crop_stride:(count_width*crop_stride) + image_crop_width]
                #plot.imshow(cropped_image)
                #plot.show()
                #print(count_width, count_height)
                #input()
                if not os.path.exists(base_Save_Directory +'/' + phonemodel):
                    os.makedirs(base_Save_Directory +'/' + phonemodel)
                plot.imsave(base_Save_Directory +'/' + phonemodel +'/' + filename + '_' + str(count_height)+str(count_width) + save_extension, cropped_image)








