# blnk-OCR
Steps to predict:
1-pip install -r requirements.txt
2-python manage.py runserver
3-Now you can go on http://127.0.0.1:8000/
4-Click on Choose File button and upload your digit image
5-click submit , The file name and predicted digit will appear 

CNN Model
-Create sequential model to add the need layers
-Convolution layer with 32 filter, size of filter is 3x3, strides = (1, 1): This specifies the step size of
 the convolutional filter, padding=’same’ This specifies how the input is padded to ensure that the filter can be applied at the edges of the image. 'same' padding means that the output of the convolutional layer will have the same spatial dimensions as the input, activation =’relu’ is used, which applies a simple thresholding operation to the output, setting any negative values to zero, input_shape (28,28,1) 28x28 is the size of image and 1 refers to 1 channel (grayscale).
-Maxpooling2d layer: Max pooling is a technique used in convolutional neural networks to reduce the spatial dimensions of the input feature maps while retaining the most important information.
-Dropout: regularization technique to avoid overfitting.
-We repeat the cycle twice again (Conv2d, Maxpooling, Dropout)
- Adding multiple Conv2D layers in a CNN model allows the network to learn increasingly complex and abstract features    from the input data.  
-Flatten layer is a type of layer in a neural network model that is used to convert the input data into a one-dimensional vector, and it is always the last layer in CNN model and the input for the fully connected layer.
-Dense layer is a type of layer in a neural network model that is used for fully connected layers. In a Dense layer, every neuron in the previous layer is connected to every neuron in the current layer, and each connection has a learnable weight
-Last layer is dense layer with 10 outputs that refers to the number of classes and with activation softmax that return the probability of the image for each class.
-Optimizer: This specifies the optimization algorithm used to update the weights of the neural network during training
-Loss: This specifies the loss function used to measure the difference between the predicted output of the model and the true target output during training.
-sparse_categorical_crossentropy is a common loss function used for multi-class classification problems where the target labels are integers.
-Metrics: This specifies the evaluation metric used to monitor the performance of the model during training and testing.



Deploy the model with django:
-Firstly, I created a virtual environment
-Install the required dependencies from requirements.txt
-Create a Django project (django-admin createproject classify)
-Create a Django app(django-admin createapp classify_app)
-Create directory template that contain the index.html 
-Copy our model ‘OCRDigit.h5’ in the same directory
-Open classify>setting.py, add the ‘classify_app’ in the installed apps, add  ‘template’ in ’DIRS’  in  TEMPLATES 
Add (STATICFILES_DIRS, STATIC_URL, MEDIA_URL, MEDIA_ROOT) at the end of the setting.py
-Open classify>urls.py, from classify_app import views
-Open classify_app>views.py, install the needed dependencies, load the model, create function makepredictions that take the file path as input  and preprocess the image then return the predicted digit, create function index that take the request as an input to deal with the requests,it returns the  predictions and file url if there is no errors,
 it renders error message if no image selected or no file selected, else it will return the html file.
-Open template>index.html, write basic html code to have a choose file button to upload image and submit button to perform the prediction function and view the filename and the predicted digit

