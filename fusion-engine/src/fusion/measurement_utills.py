import typing
from typing import Optional
from ..data_types.measurement import Measurement

class MeasurementUtill:

    def __init__(self):
        self.angle_min = 45
        self.angle_max = 135
        self.distance_min = 10
        self.distance_max = 150
        self.confidence_min = 0
        self.confidence_max = 1

    def parseJsonToMeasurement(self, json_data: dict) -> Optional[Measurement]:
        
        if not self.hasVaildField(json_data):
            return None
        if not self.hasValidData(json_data):
            return None

        return Measurement.from_json(json_data)


    def hasVaildField(self, json_data: dict) -> bool:
        required_fields = ["sensor_id", "raw_angle", "raw_distance", "timestamp", "confidence"]
        return all(field in json_data for field in required_fields)
    
    def hasValidData(self, json_data: dict) -> bool:
        try: 
            angle = float(json_data["raw_angle"])
            distance = float(json_data["raw_distance"])
            confidence = float(json_data["confidence"])
            sensor_id = int(json_data["sensor_id"])

            if not self.angle_min <= angle <= self.angle_max:
                return False
            if not self.distance_min <= distance <= self.distance_max:
                return False
            if not self.confidence_min <= confidence <= self.confidence_max:
                return False
            if not sensor_id in [1, 2]:
                return False
            return True
        except (ValueError, KeyError):
            return False