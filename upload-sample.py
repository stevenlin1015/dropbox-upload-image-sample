import io
import dropbox
import numpy as np
from PIL import Image

'''
code below refers to answer from stackflow:
https://stackoverflow.com/questions/57286114/how-to-upload-an-image-on-dropbox-using-its-api-v2-in-python
'''

if __name__ == '__main__':
    
    dbx = dropbox.Dropbox('YOUR TOKEN') # Connecting to the account
    
    image_to_upload = Image.open('YOUR_IMAGE_TO_BE_UPLOAD.jpg') # any image
    image_array_format = np.array(image_to_upload.getdata()) 
    # To transform an array into image using PIL:
    
    image_array_format = image_array_format.reshape(image_to_upload.height, image_to_upload.width, 3).astype('uint8') # unit8 is necessary to convert
    image = Image.fromarray(image_array_format).convert('RGB')
    
    # to transform the image into bytes:
    
    with io.BytesIO() as output:
        image.save(output, format="JPEG")
        upload_image = output.getvalue()
    
    # After the transformation into bytes the function works normally
    dbx.files_upload(upload_image, '/SOME_FOLDER/IMAGE_NAME.jpg', dropbox.files.WriteMode.add, mute = True)
    