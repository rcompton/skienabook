#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_skienabook
----------------------------------

Tests for `ch3.bst' module.
"""

import logging
import logging.config
import unittest

import numpy as np

from skienabook.ch3 import bst

# logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TestBst(unittest.TestCase):
    def setUp(self):
        self.test_tree = bst.BSTree(bst.BstNode(0.5))
        for xi in np.random.random(10):
            new_node = bst.BstNode(xi)
            self.test_tree.insert(new_node)
        pass

    def test_traverse(self):
        l = self.test_tree.max_first_traverse()
        logger.info(l)
        pass


if __name__ == '__main__':
    unittest.main()