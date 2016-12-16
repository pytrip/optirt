import unittest
import logging


logger = logging.getLogger(__name__)


class TestNothing(unittest.TestCase):
    def test_bla(self):
        logger.info("Testing nothing")
        self.assertTrue(True)
