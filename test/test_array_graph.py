import unittest

from src.pyinsect.documentModel.representations import DocumentNGramGraph
from src.pyinsect.structs.array_graph import ArrayGraph2D


class ArrayGraphTestCase(unittest.TestCase):
    def test_array_graph_as_document_n_gram_gram_array_divisible_by_window(self):
        train_data = [[i for i in range(9)] for j in range(9)]
    
        array_graph = ArrayGraph2D(train_data, 3)
        array_graph.as_graph(DocumentNGramGraph)

    def test_array_graph_as_document_n_gram_gram_array_not_divisible_by_window(self):
        train_data = [[i for i in range(10)] for j in range(10)]

        array_graph = ArrayGraph2D(train_data, 3)
        array_graph.as_graph(DocumentNGramGraph)
