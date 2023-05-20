from django.shortcuts import render
import cv2
from skimage import io, exposure
import keras
from PIL import Image
import numpy as np
import os
from django.core.files.storage import FileSystemStorage
# Create your views here.
media='media'
model=keras.models.load_model("DigitOCR.h5")

def makepredictions(path):
    img=Image.open(path)
    img_size = (28, 28)
    img = img.resize(img_size)
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    img = exposure.rescale_intensity(img, in_range=(0, 255), out_range=(0, 1))
    p10, p90 = np.percentile(img, (10, 90))
    img = exposure.rescale_intensity(img, in_range=(p10, p90))
    threshold_value = 0.45
    max_value = 1
    img = np.where(img < threshold_value, 0, max_value)
    img=img.astype(np.uint8)
    img=np.reshape(img,[1,28,28])
    prediction=model.predict(img,verbose=0)
    digit=int(np.argmax(prediction))
    return digit

def index(request):
    if request.method=="POST" and request.FILES['upload']:
        
	    if 'upload' not in request.FILES:
	        err='No images Selected'
	        return render(request,"index.html",{'err':err})
	    f = request.FILES['upload']
	    if f =='':
	    	err='No files selected'
	    	return render(request,"index.html",{'err':err})
	    upload =request.FILES['upload']
	    fss=FileSystemStorage()
	    file=fss.save(upload.name,upload)
	    file_url=fss.url(file)
	    predictions=makepredictions(os.path.join(media,file))
	    return render(request,"index.html",{'pred':predictions,'file_url':file_url})
    else:
	    return render(request,"index.html")