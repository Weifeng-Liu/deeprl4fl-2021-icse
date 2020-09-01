import tensorflow as tf
import keras.backend.tensorflow_backend as KTF
from keras.backend import ones_like
from keras.layers.recurrent import GRU
from keras.layers.core import Lambda
from keras.optimizers import adam
from keras.layers import Conv1D, Dense, Reshape, Concatenate, Flatten, Activation, Dropout
import numpy as np
import os



os.environ["CUDA_VISIBLE_DEVICES"] = "1"
config = tf.ConfigProto()
config.gpu_options.allow_growth=True
session = tf.Session(config=config)
KTF.set_session(session)


def fault_localization(input_length, input_dim, output_dim, hidden_dim, filters_num, kernel_val, learning_rate, drop_rate):
    input_1 = Input(shape=(input_length, input_dim))
    input_2 = Input(shape=(input_length, input_dim))
    input_3 = Input(shape=(input_length, input_dim))
    input_total = Lambda(lambda x: tf.multiply(x[0], x[1]))([input_1, input_2])
    input_total = Lambda(lambda x: tf.multiply(x[0], x[1]))([input_total, input_3])
    cnn_output = Conv1D(filters=filters_num, kernel_size=kernel_val)(input_total)
    result = Flatten()(cnn_output)
    result_fix = Dropout(rate=drop_rate)(result)
    output = Dense(output_dim)(result_fix)
    fixed_output = Activation(activation='softmax')(output)
    model = Model([input_1, input_2, input_3], fixed_output)
    ada = adam(lr=learning_rate)
    model.compile(optimizer=ada, loss='categorical_crossentropy')
    return model


def getting_data(file_path, print_text):
    print("Loading " + print_text + " Data...")
    data = np.load(file_path)
    print("Done")
    return data


fl_model = fault_localization(input_l, input_d, output_d, hidden_d, filters_n, kernel_v, learning_r, drop_r)
fl_model.fit([input_data, label_data], output_data, batch_size=batch_size_num, epochs=epoch_num)
fl_result = fl_model.predict([input_data, label_data])
final_results = np.array(fl_result)


