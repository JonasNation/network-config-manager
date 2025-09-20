#!/usr/bin/env python3
"""
Backup Handler
Handles configuration backup operations for network devices
"""

import os
from datetime import datetime
from netmiko import ConnectHandler

def create_backup_filename(device_name, backup_dir="backups"):
    """
    Create a timestamped backup filename
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = "{}_{}.txt".format(device_name, timestamp)
    filepath = os.path.join(backup_dir, filename)
    return filepath

def backup_device_config(device_info):
    """
    Backup configuration from a single device
    """
    device_name = device_info.get('name', 'unknown')
    
    try:
        print("Connecting to {}...".format(device_name))
        
        # Establish SSH connection
        connection = ConnectHandler(**device_info)
        
        # Get running configuration
        print("Retrieving configuration...")
        running_config = connection.send_command("show running-config")
        
        # Create backup file
        backup_file = create_backup_filename(device_name)
        
        # Ensure backup directory exists
        os.makedirs("backups", exist_ok=True)
        
        # Write configuration to file
        with open(backup_file, 'w') as file:
            file.write("# Configuration backup for {}\n".format(device_name))
            file.write("# Backup date: {}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            file.write("# Device: {}\n".format(device_info.get('host', 'unknown')))
            file.write("#" + "="*50 + "\n\n")
            file.write(running_config)
        
        # Close connection
        connection.disconnect()
        
        print("✅ Backup completed: {}".format(backup_file))
        return True, backup_file
        
    except Exception as error:
        print("❌ Backup failed for {}: {}".format(device_name, error))
        return False, None

def backup_multiple_devices(devices):
    """
    Backup configurations from multiple devices
    """
    successful_backups = []
    failed_backups = []
    
    print("Starting backup for {} devices...".format(len(devices)))
    print("="*50)
    
    for device in devices:
        # Add password (in real app, this would be secure)
        device['password'] = 'password'  # Placeholder
        
        success, backup_file = backup_device_config(device)
        
        if success:
            successful_backups.append((device['name'], backup_file))
        else:
            failed_backups.append(device['name'])
        
        print()  # Empty line for readability
    
    # Summary
    print("Backup Summary:")
    print("-" * 30)
    print("Successful: {}".format(len(successful_backups)))
    print("Failed: {}".format(len(failed_backups)))
    
    if successful_backups:
        print("\nSuccessful backups:")
        for name, filepath in successful_backups:
            print("  {} -> {}".format(name, filepath))
    
    if failed_backups:
        print("\nFailed backups:")
        for name in failed_backups:
            print("  {}".format(name))
    
    return successful_backups, failed_backups

if __name__ == "__main__":
    # Test backup functionality
    print("Backup Handler Test")
    print("This would test backup functionality with real devices")