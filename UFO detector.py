import random

def simulate_sensor_data():
    """
    Simulate sensor data for UFO detection.
    """
    # Simulate data from various sensors
    radar_data = random.uniform(0, 1)
    lidar_data = random.uniform(0, 1)
    infrared_data = random.uniform(0, 1)
    optical_camera_data = random.uniform(0, 1)
    
    return radar_data, lidar_data, infrared_data, optical_camera_data

def detect_ufo(radar_data, lidar_data, infrared_data, optical_camera_data):
    """
    Detect potential UFOs based on sensor data.
    """
    # Analyze sensor data for anomalies
    if radar_data > 0.9 and lidar_data > 0.8 and infrared_data > 0.7 and optical_camera_data > 0.6:
        print("Potential UFO detected!")
    else:
        print("No UFO detected.")

# Simulate sensor data
radar_data, lidar_data, infrared_data, optical_camera_data = simulate_sensor_data()

# Detect potential UFOs based on sensor data
detect_ufo(radar_data, lidar_data, infrared_data, optical_camera_data)
