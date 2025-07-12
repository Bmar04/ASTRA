from dataclasses import dataclass
from turtle import position
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

    def __init__(self):
        #Parsing sensor data to Measurment message
        parseJsonToMeasurment()

        #Check what sensor measurement is comming from
        if sensor_id == 1:
            sensor_origin = (0,0)

        #Convert raw polar coords into cart coord used to track
        position = coord.polar_to_cartesian(raw_angle, raw_distance, sensor_origin)
    
def parseJsonToMeasurment():
    