"""
A module to build simple Convolution Neural Network for Image related Deep learning experiment. 

Author: Faruk Ahmad
Date: 23 May, 2020
Ref: https://keras.io/
"""

# lets import necessary stuffs here
import tensorflow as tf
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Input, Dense, Flatten, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

def cnn_model(input_shape, num_of_class):
    """
    A method to define the CNN architecture
    """
    input = Input(shape = input_shape)

    x = Conv2D(filters = 32, kernel_size = (3, 3), strides = (1, 1), activation = "relu", padding = "valid")(input)
    x = MaxPooling2D(pool_size = (2, 2))(x)

    x = Conv2D(filters = 32, kernel_size = (3, 3), strides = (1, 1), activation = "relu", padding = "valid")(x)
    x = MaxPooling2D(pool_size = (2, 2))(x)

    x = Flatten()(x)
    x = Dense(256, activation = "relu")(x)

    output = Dense(num_of_class, activation = "softmax")(x)

    model = Model(input, output)

    model.compile(optimizer = "adam", loss = "categorical_crossentropy", metrics = ["accuracy"])

    return model



def preprocess_data(num_classes):
    # load the mnist data
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    # reshape the data
    x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
    x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

    # normalize the data
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255
    x_test /= 255

    # one hot for labels
    y_train = to_categorical(y_train, num_classes)
    y_test = to_categorical(y_test, num_classes)

    return x_train, x_test, y_train, y_test


def train_mnist(x_train, y_train, input_shape, num_classes):
    """
    a dummy method to train the built CNN model
    """
    model = cnn_model(input_shape, num_classes)

    model.fit(x_train, y_train, epochs = 1, batch_size = 32, validation_split = 0.2)

    return model

def test_mnist(x_test, y_test, model):
    loss, acc = model.evaluate(x_test, y_test)
    print(f"loss: {loss}\naccuracy: {acc}")

if __name__ == "__main__":
    input_shape = (28, 28, 1)
    num_classes = 10
    x_train, x_test, y_train, y_test = preprocess_data(num_classes)
    trained_model = train_mnist(x_train, y_train, input_shape, num_classes)
    test_mnist(x_test, y_test, trained_model)