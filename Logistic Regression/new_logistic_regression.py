from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

if __name__ == "__main__":
    # Load iris dataset
    data = datasets.load_iris(as_frame=False)
    # print(data.data)  # X
    # print(data.target)  # y
    X = data.data
    y = data.target

    # Initialize regressor model
    model = LogisticRegression(verbose=1)
    model.fit(X,y)

    # Compute score
    score = model.score(X,y)
    print("SCORE: %.2f" % score)

    # Get summary report
    ypred = model.predict(X)
    report = classification_report(y, ypred)
    print(report)

    # Get confusion matrix
    cm = confusion_matrix(y, ypred)

    # Plot confusion matrix
    fig, ax = plt.subplots(figsize=(8,6), dpi=100)
    display = ConfusionMatrixDisplay(cm, display_labels=model.classes_)
    ax.set(title="Confusion Matrix for Iris dataset")

    display.plot(ax=ax)
    plt.show()