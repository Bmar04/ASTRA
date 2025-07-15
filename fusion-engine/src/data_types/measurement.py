import socket
import json
import time
import threading
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Callable, Tuple
import sys
import os

# Import coordinates directly
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'math'))
import coordinates as coord


@dataclass
class Measurement:
    raw_angle: float
    raw_distance: float
    # timestamp in seconds
    timestamp: float
    sensor_id: int
    postion: tuple
    confidence: float
    sensor_origin: tuple

    @classmethod
    def from_json(cls, json_data: dict):
        try:
            sensor_id = int(json_data['sensor_id'])
            raw_angle = float(json_data['raw_angle'])
            raw_distance = float(json_data['raw_distance'])
            timestamp = float(json_data['timestamp'])
            confidence = float(json_data['confidence'])

            timestamp = json_data.get('timestamp', time.time())

            if sensor_id == 1:
                sensor_origin = (0, 0)
            else:
                raise ValueError(f"Invalid sensor ID: {sensor_id}")

            postion = coord.polar_to_cartesian(raw_angle, raw_distance, sensor_origin)

            return cls(
                raw_angle=raw_angle,
                raw_distance=raw_distance,
                timestamp=timestamp,
                sensor_id=sensor_id,
                postion=postion,
                confidence=confidence,
                sensor_origin=sensor_origin
            )
        except ValueError as e:
            raise e
