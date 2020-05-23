"""
A module to build simple LSTM network for Text classification related Deep learning experiment. 

Author: Faruk Ahmad
Date: 23 May, 2020
Ref: https://keras.io/
"""

# lets import necessary stuffs here
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Dropout, Embedding, Bidirectional, LSTM
from tensorflow.keras.models import Model
from tensorflow.keras.datasets import imdb
from tensorflow.keras import preprocessing

def lstm_model(max_features):
    """
    A method to define the LSTM network architecture
    You can add more layers, change the hyper parameters for further experiment
    """
    # Input for variable-length sequences of integers
    inputs = Input(shape=(None,), dtype="int32")

    # Embed each integer in a 128-dimensional vector
    x = Embedding(max_features, 128)(inputs)

    # Add 2 bidirectional LSTMs
    x = Bidirectional(LSTM(64, return_sequences=True))(x)
    x = Bidirectional(LSTM(64))(x)

    # Add a classifier
    outputs = Dense(1, activation="sigmoid")(x)
    model = Model(inputs, outputs)

    model.compile(optimizer = "adam", loss = "binary_crossentropy", metrics=["accuracy"])

    return model


def preprocess_data(maxlen, max_features):
    """
    A dummpy method to preprocess data. You can add your extrac preprocessing steps here
    """
    # lets load the data from imbd dataset
    (x_train, y_train), (x_val, y_val) = imdb.load_data(num_words=max_features)
    
    # in case of shorter sequences, lets do padding make equal length
    x_train = preprocessing.sequence.pad_sequences(x_train, maxlen=maxlen)
    x_val = preprocessing.sequence.pad_sequences(x_val, maxlen=maxlen)

    return x_train, y_train, x_val, y_val


def train_mnist(max_features, x_train, y_train):
    """
    a dummy method to train the built LSTM model
    """
    model = lstm_model(max_features)

    model.fit(x_train, y_train, epochs = 1, batch_size = 32, validation_split = 0.2)

    return model

def test_mnist(x_test, y_test, model):
    loss, acc = model.evaluate(x_test, y_test)
    print(f"loss: {loss}\naccuracy: {acc}")



if __name__ == "__main__":
    max_features = 20000  # Only consider the top 20k words
    maxlen = 200  # Only consider the first 200 words of each movie review

    x_train, y_train, x_val, y_val = preprocess_data(maxlen, max_features)
    trained_model = train_mnist(max_features, x_train, y_train)
    test_mnist(x_val, y_val, trained_model)