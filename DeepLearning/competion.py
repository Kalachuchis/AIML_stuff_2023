import tensorflow as tf
import numpy as np


class ExerciseCompClass:
    def __init__(self):
        self.saved_model = tf.keras.models.load_model("./model/")

    def predict_from_base_model(self, X: np.array, y: np.array):

        number_of_x = X.shape[1]
        X_shape = X.shape[1:]
        X = X/255

        if X_shape != (200,200):
            raise ValueError('Image size must be 200x200')
        self.saved_model.evaluate(X, y)

        return

if __name__ == "__main__":
    exer_model = ExerciseCompClass()
    # X = np.load('./X_test.npy')
    # y = np.load('./y_test.npy')
    X = np.load('./lego_x_gray_test.npy')
    y = np.load('./lego_y_test.npy')
    y = y -1

    exer_model.predict_from_base_model(X,y)