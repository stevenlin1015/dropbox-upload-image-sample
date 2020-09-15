----
## 關於本專案

This repository includes a python sample code where it can upload JPEG image to your Dropbox.

Codes are modified from [here](https://stackoverflow.com/questions/57286114/how-to-upload-an-image-on-dropbox-using-its-api-v2-in-python)

For more information,
see [Dropbox for Python Developers](https://www.dropbox.com/developers/documentation/python)

see [Dropbox for Python SDK](https://dropbox-sdk-python.readthedocs.io/en/latest/)

----
## 使用方式
**1. 需要先建立一個Dropbox TOKEN，可以到 [這裡](https://www.dropbox.com/developers/apps) 來建立一組TOKEN**

**2. 需要預先安裝for Python的Dropbox套件**

>註 : 詳細安裝方式可以參考[官網](https://www.dropbox.com/developers/documentation/python#install)

**使用pip安裝**
```bash
$ pip install dropbox
```

**使用conda安裝**
```bash
$ conda install -c anaconda dropbox
```

1. 套件安裝完後，將這個專案下載到自己的目錄下。

2. 按照自己在Dropbox API 的TOKEN，貼到程式碼的"YOUR TOKEN"這行字串中:
```bash
dbx = dropbox.Dropbox('YOUR TOKEN') # Connecting to the account
```

3. 根據自己的需求，可以自行修改主程式碼。唯一需要注意的是照片的輸入檔名跟輸出位置一定要修改到。
```bash
# 省略...
image_to_upload = Image.open('YOUR_IMAGE_TO_BE_UPLOAD.jpg') # any image
# 省略...
dbx.files_upload(upload_image, '/SOME_FOLDER/IMAGE_NAME.jpg', dropbox.files.WriteMode.add, mute = True)
```
