#!/usr/bin/env python3
"""
Network Configuration Manager
Main application entry point
"""

import argparse
import sys
from src.device_connector import test_device_connection
from src.config_reader import load_devices, display_devices
from src.backup_handler import backup_device_config, backup_multiple_devices

def main():
    parser = argparse.ArgumentParser(description='Network Configuration Manager')
    parser.add_argument('--test', action='store_true', 
                       help='Test device connection')
    parser.add_argument('--backup', action='store_true',
                       help='Backup device configurations')
    parser.add_argument('--list', action='store_true',
                       help='List all devices in inventory')
    parser.add_argument('--device', type=str,
                       help='Specify device name for operations')
    parser.add_argument('--all', action='store_true',
                       help='Apply operation to all devices')
    
    args = parser.parse_args()
    
    print("Network Configuration Manager v1.0")
    print("=" * 50)
    
    # Load devices from configuration
    devices = load_devices()
    
    if not devices:
        print("No devices found. Please check your configuration file.")
        return
    
    if args.list:
        display_devices(devices)
    
    elif args.test:
        if args.device:
            # Test specific device
            device = find_device_by_name(devices, args.device)
            if device:
                print("Testing connection to: {}".format(device['name']))
                # Add password (in real app, this would be secure)
                device['password'] = 'password'  # Placeholder
                test_device_connection(device)
            else:
                print("Device '{}' not found in inventory".format(args.device))
        else:
            print("Available devices:")
            for device in devices:
                print("  - {}".format(device['name']))
            print("\nUse --device <name> to test a specific device")
    
    elif args.backup:
        if args.all:
            # Backup all devices
            print("Backing up ALL devices...")
            backup_multiple_devices(devices)
        elif args.device:
            # Backup specific device
            device = find_device_by_name(devices, args.device)
            if device:
                print("Backing up device: {}".format(device['name']))
                # Add password (in real app, this would be secure)
                device['password'] = 'password'  # Placeholder
                backup_device_config(device)
            else:
                print("Device '{}' not found in inventory".format(args.device))
        else:
            print("Available devices:")
            for device in devices:
                print("  - {}".format(device['name']))
            print("\nOptions:")
            print("  --backup --device <name>  : Backup specific device")
            print("  --backup --all           : Backup all devices")
    
    else:
        print("Available commands:")
        print("  --list                    : Show device inventory")
        print("  --test --device <name>    : Test connection to device")
        print("  --backup --device <name>  : Backup specific device")
        print("  --backup --all           : Backup all devices")
        print("\nUse --help for detailed options")

def find_device_by_name(devices, name):
    """
    Find a device by name in the devices list
    """
    for device in devices:
        if device.get('name') == name:
            return device
    return None

if __name__ == "__main__":
    main()