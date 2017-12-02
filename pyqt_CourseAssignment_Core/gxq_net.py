import numpy as np
import os
import csv
import cv2
from glob import glob
import random
import keras
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.optimizers import SGD,RMSprop,adam
from keras.preprocessing.image import ImageDataGenerator
import Config

config = Config.Config()
Train_data_start = config.traindata_start
Train_data_end = config.traindata_end
Test_data_start = config.testdata_start
Test_data_end = config.testdata_end
Val_data_start = config.valdata_start
Val_data_end = config.valdata_end
Train_data_path = config.Train_data_path
Train_label_path = config.Train_label_path
Test_data_path = config.Test_data_path
Test_label_path = config.Test_label_path
model_save_path = config.model_save_path
Val_data_path = config.Val_data_path
Val_label_path = config.Val_label_path

def save_data(data_start,data_end,data_path,label_path):
    img_cols = config.img_cols
    img_rows = config.img_rows

    lines=[]
    with open(r'/storage/litong/data/train.csv') as f:
        csvReader=csv.reader(f)
        for line in csvReader:
            lines.append(line)
    filelist=glob(r'/storage/litong/data/train/*.jpeg')
    root=r'/storage/litong/data/train/'
    train_set_names=lines[data_start:data_end+1]
    train_set,train_label=[],[]
    for filename in train_set_names:
    	image_id=filename[0]+r'.jpeg'
    	image_label=int(filename[1])
    	image_path=os.path.join(root,image_id)
    	assert image_path in filelist
    	train_set.append(image_path)
    	train_label.append(image_label)

    Train_mean = np.array([[[[81.384773,  57.454021,  41.491707]]*224]*224]).transpose((0,3,1,2))
    Train = np.zeros((len(train_set),3,img_cols,img_rows),dtype = np.float32)
    Train_label = np.zeros((len(train_set)),dtype=int)

    for i in range(len(train_set)):
        img = cv2.imread(train_set[i],3)
        resize = cv2.resize(img,(img_cols,img_rows))
        resize = resize[:,:,::-1].transpose((2,0,1))-Train_mean
        Train[i] = resize
        Train_label[i]=train_label[i]        

    Train = 0.2989 * Train[:,0,:,:] + 0.5870 * Train[:,1,:,:] + 0.1140 * Train[:,2,:,:]
    Train = Train.reshape(Train.shape[0],img_cols,img_rows,1)

    np.save(data_path,Train)
    np.save(label_path,Train_label)
    print('Well down!')
    return Train,Train_label

def train_model():
    img_cols = config.img_cols
    img_rows = config.img_rows
    train_new_data = config.train_new_data
    if train_new_data:
        X_train,y_train = save_data(Train_data_start,Train_data_end,Train_data_path,Train_label_path)
        X_test,y_test = save_data(Test_data_start,Test_data_end,Test_data_path,Test_label_path)
    else:
        X_train = np.load(Train_data_path)
        y_train = np.load(Train_label_path)
        X_test = np.load(Test_data_path)
        y_test = np.load(Test_label_path)
#    X_train = X_train.reshape(X_train.shape[0], img_cols, img_rows, 1)
#    X_test = X_test.reshape(X_test.shape[0], img_cols, img_rows, 1)
    print('Data have been prepared!')
    batch_size = 32# number of output classes
    nb_classes = 5# number of epochs to train
    nb_epoch = 5
    nb_filters = 32# size of pooling area for max pooling
    nb_pool = 2# convolution kernel size
    nb_conv = 3

    X_train = X_train.astype('float32')
    X_test = X_test.astype('float32')

    X_train /= 255
    X_test /= 255

    # convert class vectors to binary class matrices
    Y_train = np_utils.to_categorical(y_train, nb_classes)
    Y_test = np_utils.to_categorical(y_test, nb_classes)

    model = Sequential()

    model.add(Convolution2D(nb_filters, nb_conv, nb_conv,
                        border_mode='valid',
                        input_shape=(img_cols, img_rows, 1)))
    convout1 = Activation('relu')
    model.add(convout1)
    model.add(Convolution2D(nb_filters, nb_conv, nb_conv))
    convout2 = Activation('relu')
    model.add(convout2)
    model.add(MaxPooling2D(pool_size=(nb_pool, nb_pool)))
    model.add(Dropout(0.5))
    model.add(Flatten())
    model.add(Dense(128))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(nb_classes))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adadelta')#KERAS

    # create generators  - training data will be augmented images
    validationdatagenerator = ImageDataGenerator()
    traindatagenerator = ImageDataGenerator(width_shift_range=0.1,height_shift_range=0.1,rotation_range=15,zoom_range=0.1 )

    batchsize=32
    train_generator=traindatagenerator.flow(X_train, Y_train, batch_size=batchsize)
    validation_generator=validationdatagenerator.flow(X_test, Y_test,batch_size=batchsize)
    model.fit_generator(train_generator, steps_per_epoch=int(len(X_train)/batchsize), epochs=3, validation_data=validation_generator, validation_steps=int(len(X_test)/batchsize))
    model.save(model_save_path)
    score = model.evaluate(X_test, Y_test, verbose=0)
    print(score)

def model_batch_test():
    test_new_data = config.test_new_data
    if test_new_data:
        Val,Val_label =  save_data(Val_data_start,Val_data_end,Val_data_path,Val_label_path)
    else:
        Val = np.load(Val_data_path)
        Val_label = np.load(Val_label_path)
    model = keras.models.load_model(model_save_path)
    test_results = np.zeros((2,len(Val_label)))
    test_results[1,0:len(Val_label)] = np.argmax(model.predict(Val),1)
    test_results[0,0:len(Val_label)] = np.array(Val_label)
    test_results = test_results.astype('int')

    score = 0
    for j in range(len(test_results[0,:])):
        if test_results[0,j] == test_results[1,j]:
            score += 1
    Accuracy = score/len(test_results[0,:])

    print ('======== Results========')
    print ('Accuracy: ' + str(Accuracy))
    print ('======== End ========')
    return Accuracy

def model_predict_image():
    image_path = config.image_path
    image_name = config.image_name
    lines1=[]
    with open(r'/storage/litong/data/train.csv') as f:
        csvReader=csv.reader(f)
        for line in csvReader:
            lines1.append(line)
    lines = np.array(lines1)
    a = lines[:,0]
    lin = []
    for i in range(len(a)):
        lin.append(a[i])
    file_index = lin.index(image_name)
    image_label = lines[file_index,1]
    image_path = image_path+image_name+'.jpeg'

    Val_mean = np.array([[[[81.384773,  57.454021,  41.491707]]*224]*224]).transpose((0,3,1,2))
    Val = np.zeros((1,3,224,224),dtype = np.float32)
    img = cv2.imread(image_path, 3)
    resize = cv2.resize(img,(224,224))
    resize = resize[:,:,::-1].transpose((2,0,1))-Val_mean
    Val = resize
    Val = 0.2989 * Val[:,0,:,:] + 0.5870 * Val[:,1,:,:] + 0.1140 * Val[:,2,:,:]
    Val = Val.reshape(Val.shape[0],224,224,1)

    model = keras.models.load_model(model_save_path)
    test_results = np.argmax(model.predict(Val),1)

    print('correct result:',image_label)
    print('presict result:',test_results)
    return test_results










