import math
import numpy as np

#Converts polar coordinates to cartesian coordinates
def polar_to_cartesian(angle: float, radius: float, sensor_origin: tuple) -> tuple:
    # Shift angle by +π/2 so 0 is "up" (y-axis)
    shifted_angle = angle + math.pi / 2
    x = radius * math.cos(shifted_angle) + sensor_origin[0]
    y = radius * math.sin(shifted_angle) + sensor_origin[1]
    return (x, y)

#Converts cartesian coordinates to polar coordinates
def cartesian_to_polar(x: float, y: float, sensor_origin: tuple) -> tuple:
    angle = math.atan2(y - sensor_origin[1], x - sensor_origin[0])
    radius = math.sqrt((x - sensor_origin[0])**2 + (y - sensor_origin[1])**2)
    return (angle, radius)

#Rotates a covariance matrix
def rotate_covariance(covariance_matrix: np.ndarray, angle: float) -> np.ndarray:
    rotation_matrix = np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])
    return rotation_matrix @ covariance_matrix @ rotation_matrix.T

#Calculates the jacobian of the measurement function
def measure_jacobian(x: float, y: float, sensor_origin: tuple) -> np.ndarray:
    return np.array([[1, 0, -y], [0, 1, x], [0, 0, 1]])
 