import numpy as np

from scipy import stats
from sklearn import datasets
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report


def trainBaggingLogReg(sampleProp, ensembleSize, Xtrain, Xtest, Ytrain, Ytest):
    """
    Select a classification dataset. Create a function trainBaggingLogReg(sampleProp, ensembleSize, Xtrain, Xtest, Ytrain, Ytest) with the following input and output values:
        Inputs:
        sampleProp - real number from 0 to 1, representing the fraction of the training set you use for each model in the ensemble
        ensembleSize - the number of models that make up your ensemble
        Xtrain, Xtest, Ytrain, Ytest - the training and test datasets
    Output:
        ensemble - a dictionary containing the following
        individualResults - a list containing the performance metrics of each individual model
        ensembleModels - a list of the models in the ensemble
        ensembleResults - the performance metrics of the ensemble
    """
    ensemble = {}
    individualResults = []
    ensembleModels = []

    # Train and test individual models
    for i in range(ensembleSize):
        # Create a bagging classifier with a logistic regression base estimator
        # bagging_clf = BaggingClassifier(
        #     LogisticRegression(max_iter=10000),
        #     n_estimators=1,
        #     max_samples=sampleProp,
        #     bootstrap=True,
        #     random_state=i,
        # )

        # Train the model on a randomly selected subset of the training data
        training_index = np.random.choice(len(Xtrain), int(sampleProp*len(Xtrain)), replace=True)
        Xtrain_subset = Xtrain[training_index]
        Ytrain_subset = Ytrain[training_index]

        model = LogisticRegression()
        model.fit(Xtrain_subset, Ytrain_subset)
        # Make predictions on the test data
        y_pred = model.predict(Xtest)

        # Calculate performance metrics
        accuracy = accuracy_score(Ytest, y_pred)
        precision = precision_score(Ytest, y_pred, average='micro')
        recall = recall_score(Ytest, y_pred, average='micro')
        f1 = f1_score(Ytest, y_pred, average='micro')

        # Use classification_report
        report = classification_report(Ytest, y_pred, output_dict=True)

        # Store the individual model's performance metrics
        # individualResults.append(
        #     {"accuracy": accuracy, "precision": precision, "recall": recall, "f1": f1}
        # )
        individualResults.append(report)

        # Store the individual model
        # ensembleModels.append(bagging_clf)
        ensembleModels.append(model)


    # Calculate ensemble performance metrics
    y_pred_ensemble = []

    for i in range(len(Xtest)):
        predictions = [model.predict([Xtest[i]])[0] for model in ensembleModels]
        # Determines the mode for the numpy array
        predictions_majority = max(set(predictions), key=predictions.count)
        y_pred_ensemble.append(predictions_majority)

    ensembleAccuracy = accuracy_score(Ytest, y_pred_ensemble)
    ensemblePrecision = precision_score(Ytest, y_pred_ensemble, average='micro')
    ensembleRecall = recall_score(Ytest, y_pred_ensemble, average='micro')
    ensembleF1 = f1_score(Ytest, y_pred_ensemble, average='micro')

    ensembleSummary = classification_report(Ytest, y_pred_ensemble, output_dict=True)

    # Store the ensemble performance metrics
    ensembleResults = {
        "accuracy": ensembleAccuracy,
        "precision": ensemblePrecision,
        "recall": ensembleRecall,
        "f1": ensembleF1,
    }

    # Store the ensemble dictionary and return it
    ensemble = {
        "individualResults": individualResults,
        "ensembleModels": ensembleModels,
        "ensembleResults": ensembleSummary,
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

    bagging_log = (trainBaggingLogReg(0.5, 5, X_train, X_test, y_train, y_test))
        
