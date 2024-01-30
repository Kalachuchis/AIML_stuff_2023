from unittest import TestCase
from script import compute_accuracy


class TestHandler(TestCase):
    def test_identical_list(self):
        labels = ["a", "b", "c", "d"]
        preds = ["a", "b", "c", "d"]
        self.assertEqual(compute_accuracy(labels, preds), 1)

    def test_some_identical_list(self):
        labels = ["a", "b", "e", "f"]
        preds = ["a", "b", "c", "d"]
        assertion = 0 < compute_accuracy(labels, preds) < 1
        self.assertEqual(compute_accuracy(labels, preds), 0.5)

    def test_no_identical_list(self):
        labels = ["a", "b", "c", "d"]
        preds = ["e", "f", "g", "h"]
        self.assertEqual(compute_accuracy(labels, preds), 0)

    def test_length_error(self):
        labels = ["a", "b", "c", "d", "e"]
        preds = ["a", "b", "c", "d"]
        with self.assertRaises(ValueError) as err_context:
            compute_accuracy(labels, preds)

    def test_empty_list(self):
        labels = []
        preds = []
        with self.assertRaises(ValueError) as err_context:
            compute_accuracy(labels, preds)
