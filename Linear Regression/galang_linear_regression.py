import numpy as np
import math

class MyLinearRegression():

    def __init__(self):
        # Initialize weights
        self.c = 0
        self.m = 0
    def compute_loss(self, ytrue, ypred):

        """ Computes the Mean Squared Error of the true values and predicted values

        Args:
            ytrue (ndarray): true values
            ypred (ndarray): predicted values

        Returns:
            float: the Mean Squared Error
        """
        rmse = math.sqrt(np.square(np.subtract(ytrue, ypred)).mean())

        return rmse


        pass
    
    def compute_gradient(self, X, ytrue, ypred):
        """ Computes the gradient using the inputs 'X' and 'ytrue', and the predicted outputs 'ypred' of the current weights 
            The gradients are the partial derivatives of the loss with respect to each of the weights

        Args:
            X (ndarray): numpy array of the independent variable
            ytrue (ndarray): true values
            ypred (ndarray): predicted values

        Returns:
            (float, float): tuple of floats representing the gradient for the two weights
        """
        dm = (-2) * (X * (ytrue - ypred)).mean()
        dc= (-2) * ((ytrue - ypred)).mean()

        return dc, dm
        pass

    def fit(self, X, y, learning_rate, epochs):
        """ Performs basic linear regression on the input data

        Args:
            X (ndarray): numpy array of the independent variable
            y (ndarray): numpy array of the dependent variable
            learning_rate (float): learning rate
            epochs (int): number of times gradient descent will be performed
        """

        # Iterate over the number of epochs. For each iter, do the ff:
        for i in list(range(1,epochs+1)):
        #   STEP 1: Compute the predicted output given the weights
            print(f'Epoch {i}')
            ypreds = (self.m * X) + self.c
        #   STEP 2: Compute the loss using the class method
            loss = self.compute_loss(y, ypreds)
            print("RMSE", loss)
        #   STEP 3: Compute the gradients of the weights using the class method
            dc, dm = self.compute_gradient(X, y, ypreds)
            print(dc, dm)
        #   STEP 4: Update the weights using the gradients and learning rate
            self.m = self.m - (learning_rate* dm)
            self.c = self.c - (learning_rate* dc)
            print('m', self.m)
            print('c', self.c)
            print()




linear_regression = MyLinearRegression()


X = np.array([60, 74, 46, 102])
y = np.array([48, 54, 44, 120])

linear_regression.fit(X,y, 0.0001, 20)