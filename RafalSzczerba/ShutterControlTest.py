import json
import unittest
import ShuttersControl  as shutters

class AdditionTestCase(unittest.TestCase):

    def test_ReadValueInRange(self):
        result = shutters.ReadLevel()
        assert json.loads(result)["status"] == "ok"
if __name__ == '__main__':
    unittest.main()



