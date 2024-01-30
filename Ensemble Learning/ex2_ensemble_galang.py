import numpy as np

from sklearn import datasets
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report


def trainBoostingLogReg(sampleProp, ensembleSize, Xtrain, Xtest, Ytrain, Ytest):
    """
    Select a classification dataset. Create a function trainBoostingLogReg(sampleProp, ensembleSize, Xtrain, Xtest, Ytrain, Ytest) with the following input and output values:
    Inputs:
        sampleProp - real number from 0 to 1, representing the fraction of the training set you use for each model in the ensemble
        ensembleSize - the number of models that make up your ensemble
        Xtrain, Xtest, Ytrain, Ytest - the training and test datasets
    Output:
        ensemble - a dictionary containing the following
        individualResults - a list containing the performance metrics of each iteration
        ensembleModels - a list of the models in the ensemble
        ensembleResults - the performance metrics of the ensemble
    """

    # Initialize variables
    ensembleModels = []
    individualResults = []
    ensemblePredictions = []
    wrongResults = []
    wrongValues = []

    # Train ensembleSize number of models
    for i in range(ensembleSize):
        # Create a subset of the training data
        n_samples = int(sampleProp * len(Xtrain))
        indices = np.random.choice(len(Xtrain), n_samples - len(wrongResults), replace=True)
        X_train_subset = Xtrain[indices]
        Y_train_subset = Ytrain[indices]
        
        X_train_subset = np.append(Xtrain[indices], wrongValues)
        Y_train_subset = np.append(Ytrain[indices], wrongResults)

        # Train a GradientBoostingClassifier model
        model = LogisticRegression(random_state=i)
        # model = GradientBoostingClassifier()
        model.fit(X_train_subset, Y_train_subset)


        # Store the individual model
        ensembleModels.append(model)

        # Make predictions on the test set
        Y_pred = model.predict(Xtest)
        ensemblePredictions.append(Y_pred)

        # Calculate the performance metrics for the individual model
        acc = accuracy_score(Ytest, Y_pred)
        prec = precision_score(Ytest, Y_pred, average='micro')
        rec = recall_score(Ytest, Y_pred, average='micro')
        f1 = f1_score(Ytest, Y_pred, average='micro')

        wrongResults = Y_pred[(Ytest != Y_pred)]
        wrongValues = Xtest[(Ytest != Y_pred)]

        # Use classification_report
        report = classification_report(Ytest, Y_pred, output_dict=True)

        # Store the performance metrics of the individual model
        # individualResults.append(
        #     {"Accuracy": acc, "Precision": prec, "Recall": rec, "F1": f1}
        # )

        individualResults.append(report)

    # # Combine the predictions of all individual models to create the ensemble
    # ensemblePredictions = np.array(ensemblePredictions)
    # ensemblePred = np.round(np.mean(ensemblePredictions, axis=0))

    # # Calculate the performance metrics for the ensemble
    # acc = accuracy_score(Ytest, ensemblePred)
    # prec = precision_score(Ytest, ensemblePred, average='micro')
    # rec = recall_score(Ytest, ensemblePred, average='micro')
    # f1 = f1_score(Ytest, ensemblePred, average='micro')

        

    # # Store the performance metrics of the ensemble
    # ensembleResults = {"Accuracy": acc, "Precision": prec, "Recall": rec, "F1": f1}

    # # Use classification_report
    # ensembleSummary = classification_report(Ytest, ensemblePred, output_dict=True)

    # Create the ensemble dictionary
    ensemble = {
        "individualResults": individualResults,
        "ensembleModels": ensembleModels,
        "ensembleResults": individualResults[-1],
    }

    return ensemble

if __name__ == "__main__":
    # Load iris dataset
    data = datasets.load_iris(as_frame=False)
    # print(data.data)  # X
    # print(data.target)  # y
    X = data.data # type: ignore
    y = data.target #type: ignore
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    bagging_log = trainBoostingLogReg(0.5, 5, X_train, X_test, y_train, y_test)
        
