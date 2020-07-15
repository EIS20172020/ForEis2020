import tensorflow as tf
from tensorflow.keras import layers


class DenseLayer(layers.Layer):
    def __init__(self, kernel, activation=None, **kwargs):
        self.kernel = kernel
        self.activation = layers.Activation(activation)
        super(DenseLayer, self).__init__(**kwargs)

    def build(self, input_shape):
        self.w = self.add_weight(name='w',
                                 shape=(input_shape[1], self.kernel),
                                 initializer='uniform',
                                 trainable=True)
        self.bias = self.add_weight(name='bias',
                                    shape=(self.kernel,),
                                    initializer='zero',
                                    trainable=True)
        super(DenseLayer, self).build(input_shape)

    def call(self, x, **kwargs):
        return self.activation(x @ self.w + self.bias)


model = tf.keras.Sequential([
    DenseLayer(20, activation='relu', input_shape=[224, ]),
    DenseLayer(10, activation='relu'),
    DenseLayer(2, activation='softmax')
])

model.summary()