#!/usr/bin/env python3
"""
Basic Network Device Connector
Simple script to test SSH connections to network devices
"""

from netmiko import ConnectHandler
import logging

# Set up basic logging
logging.basicConfig(level=logging.INFO)

def test_device_connection(device_info):
    """
    Test SSH connection to a network device
    """
    try:
        print("Attempting to connect to {}...".format(device_info['host']))
        
        # Establish SSH connection
        connection = ConnectHandler(**device_info)
        
        # Send a simple command
        output = connection.send_command("show version")
        
        print("✅ Connection successful!")
        print("Device response preview: {}...".format(output[:100]))
        
        # Close connection
        connection.disconnect()
        return True
        
    except Exception as error:
        print("❌ Connection failed: {}".format(error))
        return False

if __name__ == "__main__":
    # Example device configuration (you'll modify this later)
    device = {
        'device_type': 'cisco_ios',
        'host': '192.168.1.1',  # Replace with actual device IP
        'username': 'admin',     # Replace with actual username
        'password': 'password',  # Replace with actual password
        'timeout': 10,
    }
    
    print("Network Device Connection Test")
    print("=" * 40)
    
    result = test_device_connection(device)
    
    if result:
        print("\n🎉 Ready to build the configuration manager!")
    else:
        print("\n⚠️  Fix connection issues before proceeding.")