


import cv2 as cv
import matplotlib.pyplot as plot
import numpy as np
import os, os.path
from PIL import Image

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


# ## Parameters

# In[12]:


base_Save_Directory = '/media/rose/Windows/Cropped_Corrected/TrainDataset'
base_Load_Directory = '/media/rose/Windows/Final-Models'
save_extension = '.jpg'


(image_crop_height, image_crop_width) = (224,224)
crop_stride = 224

ManualSaveExtension = False




# ##    Iterate over all folder and Images

# In[ ]:


valid_image_extensions = [".jpg", ".jpeg"] #specify your vald extensions here
valid_image_extensions = [item.lower() for item in valid_image_extensions]

image_onprogress_number = 0
phone_onprogress_number = 0
total_phonemodel = len(os.listdir(os.path.join(base_Load_Directory)))
for phonemodel in os.listdir(os.path.join(base_Load_Directory)):
    image_onprogress_number = 0
    phone_onprogress_number += 1
    total_imagefileonPhone = len(os.listdir(os.path.join(base_Load_Directory, phonemodel)))
    for file in os.listdir(os.path.join(base_Load_Directory, phonemodel)):
        image_onprogress_number += 1
        extension = os.path.splitext(file)[1]
        filename = os.path.splitext(file)[0]
        if extension.lower() not in valid_image_extensions:
            continue
        
        image_file = os.path.join(base_Load_Directory,phonemodel,file)
        
        im = Image.open(image_file)
        #im.show()
        (image_original_width, image_original_height) = im.size
        
       

        
        number_croppedimages_in_width = (image_original_width-image_crop_width)//crop_stride + 1
        number_croppedimages_in_height = (image_original_height-image_crop_height)//crop_stride + 1
        print('Phone in Progress:'+str(phone_onprogress_number)+'/'+str(total_phonemodel))
        print(phonemodel)
        print("Photo Number on Progress:"+str(image_onprogress_number) +'/'+str(total_imagefileonPhone))
        print("Image:"+str(filename))
        print("Image Size:"+str(im.size))
        print('Number of Cropped Images in Width, Height:'+str((number_croppedimages_in_width,number_croppedimages_in_height)))
        print()
        print()
        #input()
        
        
     
        
        options={}
        if 'transparency' in im.info:
            options['transparency'] = im.info["transparency"]
            
        
        if not ManualSaveExtension:
            save_extension = extension
                   
        
        for count_height in range(number_croppedimages_in_height):
            for count_width in range(number_croppedimages_in_width):
                cropped_image = im.crop((count_width*crop_stride, count_height*crop_stride, count_width*crop_stride + image_crop_width, count_height*crop_stride+image_crop_height))
                
                #cropped_image.show()
                #print(cropped_image.shape)
                #print(count_width, count_height)
                #input()
                
                if not os.path.exists(base_Save_Directory +'/' + phonemodel):
                    os.makedirs(base_Save_Directory +'/' + phonemodel)
                #cropped_image.save("CropTest.jpg")
                cropped_image.save(base_Save_Directory + '/' + phonemodel + '/' + filename +'_'+str(count_height)+str(count_width) + save_extension, **options)
                #print(filename + '_' +str(count_height)+str(count_width) + save_extension)
                

