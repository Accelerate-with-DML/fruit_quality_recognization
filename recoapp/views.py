from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from keras.models import load_model
from keras.preprocessing.image import image_utils 
import numpy as np



# Create your views here.

def index(request):
    context= {'a':1}
    return render(request, 'index.html',context )

classes = ['Fresh Apple','Fresh Avocado','Fresh Banana','Fresh Orange','Fresh Pomegranate','Rotten Apple','Rotten Avocado','Rotten Banana','Rotten Orange','Rotten Pomegranate']

# model = load_model('./models/fruit_quality_model.h5')
 
def predictImage(request):
    fileObj = request.FILES['filePath']
    fs = FileSystemStorage()
    filePathName = fs.save(fileObj.name,fileObj)
    filePathName =fs.url(filePathName)
    testimage = '.'+filePathName


    new_model = load_model('models/fruit_quality_model.h5')
    new_model.summary()
    img = image_utils.load_img(testimage,target_size=(64,64))
    x = image_utils.img_to_array(img)
    x=x/255
    print('ddddddd',x)
    # x = np.expand_dims(testimage, axis = 0)
    x=x.reshape(1,64,64,3)
    print('ssssss',x)
    result = new_model.predict(x)
    print('aaaaaa')
    print(result)
    print('bbbbb')
    result=np.argmax(result)
    print(result)
    if result == 0 :
        prediction = classes[0]
    elif result == 1:
        prediction = classes[1]
    elif result ==2:
        prediction = classes[2]
    elif result == 3:
        prediction = classes[3]
    elif result ==4:
        prediction = classes[4]
    elif result == 5:
        prediction = classes[5]
    elif result == 6:
        prediction = classes[6]
    elif result == 7:
        prediction = classes[7]   
    elif result == 8:
        prediction = classes[8]
    else:
        prediction = classes[9]


    context={'filePathName':filePathName , 'predction':prediction}
    return render(request,'index.html', context)
import os
def DataBase(request):
    listOfImages=os.listdir('./media/')
    listOfImagesPath=['./media/'+i for i in listOfImages]
    context ={'listOfImagesPath':listOfImagesPath}
    return render(request,'viewDB.html',context)