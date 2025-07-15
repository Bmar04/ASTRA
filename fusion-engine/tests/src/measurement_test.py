import unittest
import sys
import os
from datetime import datetime

# Add the fusion-engine directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from src.data_types.measurement import Measurement

class TestMeasurement(unittest.TestCase):

    json_data = {
        "sensor_id": 1,
        "raw_angle": 65.5,
        "raw_distance": 100,
        "timestamp": 1715769600,
        "confidence": 0.9
    }

    def test_valid_object_from_json(self):
        measurement = Measurement.from_json(self.json_data)
        self.assertEqual(measurement.sensor_id, 1) 
        self.assertEqual(measurement.raw_angle, 65.5)
        self.assertEqual(measurement.raw_distance, 100)
        self.assertEqual(measurement.timestamp, 1715769600)
        self.assertEqual(measurement.confidence, 0.9)

        self.assertIsInstance(measurement.postion, tuple)
        self.assertEqual(measurement.postion, (-45.595569022149476,-89.00024767126439))

if __name__ == "__main__":
    unittest.main()