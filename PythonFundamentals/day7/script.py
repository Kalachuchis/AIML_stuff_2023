from ps_2_unit_test_Galang import InsecurityBank


def compute_accuracy(labels, preds):
    n = len(labels)
    if len(labels) != len(preds):
        raise ValueError("Labels and preds should be same length")
    correct = len([preds[i] for i in range(n) if preds[i] == labels[i]])
    return correct / n

