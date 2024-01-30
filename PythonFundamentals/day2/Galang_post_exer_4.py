labels = input("labels: ").strip().split(" ")
predictions = input("preds: ").strip().split(" ")


try:
    if len(labels) != len(predictions):
        raise ValueError("length not same")
    # len([(l, p) for l, p in zip(labels, predictions) if l == p]) / len(labels)
    # adds to list if l is equal to p
    print(
            f"{(len([(l, p) for l, p in zip(labels, predictions) if l == p]) / len(labels)) *100}%"
    )
except Exception as e:
    print(e)
