import unittest
from engine import Engine


class EngineTestCase(unittest.TestCase):
    def test_init_engine(self):
        engine = Engine()
        self.assertTrue(engine)

    def test_execute(self):
        engine = Engine()
        engine.execute()
        self.assertTrue(True)