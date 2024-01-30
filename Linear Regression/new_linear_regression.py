import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn import datasets

def train_regression(X, y):
    # Initialize regressor
    regressor = LinearRegression()
    # Fit model
    model = regressor.fit(X, y)
    # Get performance score
    r2 = model.score(X, y)

    print("R-squared: %.3f" % r2)
    print(f"Model weights: {model.coef_}")
    print(f"Model bias: {model.intercept_}")

    return model

def train_poly_regression(X, y):
    # Init polynomial transformer
    transformer = PolynomialFeatures(degree=9, include_bias=True)
    
    # Fit transformer and create new input array with polynomial features
    X_poly = transformer.fit_transform(X)
    # Init linear regressor
    regressor = LinearRegression()
    model = regressor.fit(X_poly, y)
    # Get R-squared
    r2 = model.score(X_poly, y)
    print("Model R-squared: %.3f" % r2)

    return model, transformer

if __name__ == "__main__":
    # # Load dataset
    data = datasets.load_diabetes(as_frame=False, scaled=True)
    X = data.data
    y = data.target

    Xtrain, Xtest, ytrain, ytest = train_test_split(
        X, y, test_size=0.25
    )

    print(Xtrain.shape)
    print(ytrain.shape)
    print(Xtest.shape)
    print(ytest.shape)

    # model = train_regression(Xtrain, ytrain)
    model, transformer = train_poly_regression(Xtrain, ytrain)
    Xtest_poly = transformer.fit_transform(Xtest)
    ypred = model.predict(Xtest_poly)
    r2 = r2_score(ytest, ypred)
    print("Test R-squared: %.3f" % (r2))

    # model, transformer = train_poly_regression(X, y)
    # input_x = X[0,:].reshape(1,-1)
    # # Perform polynomial transform to data when predicting
    # input_x = transformer.fit_transform(input_x)
    # output_y = model.predict(input_x)
    # print(output_y)
    # print(y[0])

    # X = np.array([60, 74, 46, 102])
    # Y = np.array([48, 54, 44, 120])

    # model = train_regression(X.reshape(-1,1), Y)

    