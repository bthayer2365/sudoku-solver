"""Tests for sudokulib.solvers"""
from unittest import TestCase

from sudokulib.layer import Layer
from sudokulib.preprocessors import LineBlockPreprocessor
from sudokulib.preprocessors import BlockBlockPreprocessor

SOLUTION = ' ' * 81


class LineBlockPreprocessorTestCase(TestCase):
    """Tests for LineBlockPreprocessor"""

    def test_preprocess_horizontal(self):
        preprocessor = LineBlockPreprocessor()

        data = '29X7X5X481XX6892738X7X249X5XXX2X1XXXXX24X' \
               '68XXXX98X342X9XX5X2XX44XXXX8X92321947586'

        layer = Layer(data, SOLUTION)
        self.assertEquals(layer._candidates[27], set(['5', '6', '7']))
        self.assertEquals(layer._candidates[28], set(['3', '4', '5',
                                                      '6', '7', '8']))
        self.assertEquals(layer._candidates[29], set(['3', '4', '5',
                                                      '6', '8']))
        self.assertEquals(layer._candidates[33], set(['3', '6', '7']))
        self.assertEquals(layer._candidates[34], set(['3', '5', '6']))
        self.assertEquals(layer._candidates[35], set(['7', '9']))

        layer = preprocessor.preprocess(layer)
        self.assertEquals(layer._candidates[27], set(['5', '7']))
        self.assertEquals(layer._candidates[28], set(['3', '4', '5',
                                                      '7', '8']))
        self.assertEquals(layer._candidates[29], set(['3', '4', '5', '8']))
        self.assertEquals(layer._candidates[33], set(['3', '6', '7']))
        self.assertEquals(layer._candidates[34], set(['3', '5', '6']))
        self.assertEquals(layer._candidates[35], set(['7', '9']))

    def test_preprocess_vertical(self):
        preprocessor = LineBlockPreprocessor()

        data = '29X7X5X481XX6892738X7X249X5XXX2X1XXXXX24X' \
               '68XX6X98X342X9XX5X2XX44XXXX8X92321947586'

        layer = Layer(data, SOLUTION)
        self.assertEquals(layer._candidates[28], set(['3', '4', '5',
                                                      '7', '8']))
        self.assertEquals(layer._candidates[37], set(['1', '3', '5', '7']))
        self.assertEquals(layer._candidates[46], set(['1', '5', '7']))
        self.assertEquals(layer._candidates[55], set(['6', '7', '8']))
        self.assertEquals(layer._candidates[64], set(['5', '6', '7']))

        layer = preprocessor.preprocess(layer)
        self.assertEquals(layer._candidates[28], set(['3', '4', '5', '8']))
        self.assertEquals(layer._candidates[37], set(['1', '3', '5']))
        self.assertEquals(layer._candidates[46], set(['1', '5']))
        self.assertEquals(layer._candidates[55], set(['6', '7', '8']))
        self.assertEquals(layer._candidates[64], set(['5', '6', '7']))


class BlockBlockPreprocessorTestCase(TestCase):
    """Tests for BlockBlockPreprocessor"""

    def test_preprocess_horizontal(self):
        preprocessor = BlockBlockPreprocessor()

        data = 'XX5X7X89XX198X2XX5487XXXXX2XX3XXX5X8954X8' \
               'XX26XX8XXX9XX541798263732465189896X2X457'

        layer = Layer(data, SOLUTION)
        self.assertEquals(layer._candidates[30], set(['1', '2', '6', '9']))
        self.assertEquals(layer._candidates[31], set(['1', '4']))
        self.assertEquals(layer._candidates[32], set(['1', '4', '6',
                                                      '7', '9']))
        self.assertEquals(layer._candidates[48], set(['1', '2', '3',
                                                      '5', '6']))
        self.assertEquals(layer._candidates[49], set(['1', '3', '4', '5']))
        self.assertEquals(layer._candidates[50], set(['1', '3', '4',
                                                      '6', '7']))

        layer = preprocessor.preprocess(layer)
        self.assertEquals(layer._candidates[30], set(['2', '6', '9']))
        self.assertEquals(layer._candidates[31], set(['4']))
        self.assertEquals(layer._candidates[32], set(['4', '6', '9']))
        self.assertEquals(layer._candidates[48], set(['2', '3', '5', '6']))
        self.assertEquals(layer._candidates[49], set(['3', '4', '5']))
        self.assertEquals(layer._candidates[50], set(['3', '4', '6']))

    def test_preprocess_vertical(self):
        preprocessor = BlockBlockPreprocessor()

        data = '29X7X5X481XX6892738X7X249X5XXX2X1XXXXX24X' \
               '68XX6X98X342X9XX5X2XX44XXXX8X92321947586'

        layer = Layer(data, SOLUTION)
        layer = LineBlockPreprocessor().preprocess(layer)
        layer = LineBlockPreprocessor().preprocess(layer)
        self.assertEquals(layer._candidates[28], set(['3', '4', '5', '8']))
        self.assertEquals(layer._candidates[29], set(['3', '4', '5', '8']))
        self.assertEquals(layer._candidates[37], set(['1', '3', '5']))
        self.assertEquals(layer._candidates[46], set(['1', '5']))

        layer = preprocessor.preprocess(layer)
        self.assertEquals(layer._candidates[28], set(['3', '4', '8']))
        self.assertEquals(layer._candidates[29], set(['3', '4', '8']))
        self.assertEquals(layer._candidates[37], set(['1', '3']))
        self.assertEquals(layer._candidates[46], set(['1']))