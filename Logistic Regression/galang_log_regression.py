import numpy as np



class MyLogisticRegression():

    def __init__(self):
        # Initialize weights
        self.m = 1
        self.c = 1
        pass

    def fit(self, X, y, learning_rate, epochs):
        """ Performs basic logistic regression on the input data

        Args:
            X (ndarray): 1-dimensional numpy array of the independent variable
            y (ndarray): numpy array of the dependent variable
            learning_rate (float): learning rate
            epochs (int): number of times gradient descent will be performed
        """

        # Iterate over the number of epochs. For each iter, do the ff:
        for i in list(range(1, epochs+1)):
            #   STEP 1: Compute the predicted output given the weights.
            #           Predict using the linear equation then apply the Sigmoid method
            
            print(f'Epoch {i}')
            sigmoid_x = self._sigmoid(X)
            print(f'Current Y predictions:\n{sigmoid_x}')

            #   STEP 2: Compute the loss using the class method
            loss = self.compute_loss(y, sigmoid_x)
            print(f'Loss: {loss}')
            
            #   STEP 3: Compute the gradients of the weights using the class method
            dc, dm = self.compute_gradient(X, y, sigmoid_x)
            print(f'Dc: {dc}')
            print(f'Dm: {dm}')

            #   STEP 4: Update the weights using the gradients and learning rate
            self.m = self.m - (learning_rate * dm)
            self.c = self.c - (learning_rate * dc)
            print(f"Current M: {self.m}")
            print(f"Current C: {self.c}")
            print("=====================================================")

    def compute_loss(self, ytrue, ypred):
        """ Computes the Log-Likelihood Error of the true values and predicted values

        Args:
            ytrue (ndarray): true values
            ypred (ndarray): predicted values

        Returns:
            float: the Log-Likelihood Error
        """
        loss = (ytrue * (np.log(ypred)) + (1 - ytrue)* np.log(1- ypred)).mean()
        
        return -loss

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

        dm = (X*(ypred-ytrue)).mean()
        dc = (ypred - ytrue).mean()

        return dc, dm

    def _sigmoid(self, arr):
        """ Applies the Sigmoid function to each element of the input array

        Args:
            arr (ndarray): input numpy array

        Returns:
            (ndarray): numpy array containing the Sigmoid-transformed elements of the input array
        """
        linear_f_x = self.m*arr + self.c
        log_f_x = 1 / (1 + np.exp(-(linear_f_x)))

        return log_f_x

    def predict(self, X):
        """ Predicts the classes of the given input X using the trained weights.
            Use a Decision Boundary of 0.5. The output array should contain either 0 or 1

        Args:
            X (ndarray): input array

        Returns
            (ndarray): output array of the classification of the input. Values should be 0 or 1
        """

        y_preds = self._sigmoid(X)
        y_preds[y_preds >= 0.5] = 1
        y_preds[y_preds < 0.5] = 0

        return  y_preds

if __name__ == "__main__":
    # Load data
    X = np.load("dummy_log_X.npy")
    y = np.load("dummy_log_y.npy")
    # Set learning rate and epochs
    L = 0.001
    epochs = 100
    # Train
    regressor = MyLogisticRegression()
    regressor.fit(X, y, L, epochs)
    # Predict
    input_X = np.array([-1.01, 0.24, 2.23])
    ypred = regressor.predict(input_X)
    print(ypred)