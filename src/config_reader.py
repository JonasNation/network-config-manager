#!/usr/bin/env python3
"""
Configuration Reader
Handles reading device inventory from YAML files
"""

import yaml
import os

def load_devices(config_file="configs/devices.yaml"):
    """
    Load device inventory from YAML file
    Returns list of device dictionaries
    """
    try:
        # Check if file exists
        if not os.path.exists(config_file):
            print("Error: Configuration file {} not found".format(config_file))
            return []
        
        # Read and parse YAML file
        with open(config_file, 'r') as file:
            config_data = yaml.safe_load(file)
        
        # Extract devices list
        devices = config_data.get('devices', [])
        
        print("Loaded {} devices from configuration".format(len(devices)))
        return devices
        
    except yaml.YAMLError as error:
        print("Error parsing YAML file: {}".format(error))
        return []
    except Exception as error:
        print("Error loading configuration: {}".format(error))
        return []

def display_devices(devices):
    """
    Display device inventory in a readable format
    """
    if not devices:
        print("No devices found in configuration")
        return
    
    print("\nDevice Inventory:")
    print("-" * 50)
    
    for i, device in enumerate(devices, 1):
        print("{}. Name: {}".format(i, device.get('name', 'Unknown')))
        print("   Host: {}".format(device.get('host', 'Unknown')))
        print("   Type: {}".format(device.get('device_type', 'Unknown')))
        print("   Description: {}".format(device.get('description', 'No description')))
        print()

if __name__ == "__main__":
    # Test the configuration reader
    devices = load_devices()
    display_devices(devices)