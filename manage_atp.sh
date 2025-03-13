#!/bin/bash

# Check if the script is run as root
if [ "$EUID" -ne 0 ]; then
    echo "Error: Please run this script as root."
    exit 1
fi

# Uninstall unused dependencies
echo "Removing unused dependencies..."
apt autoremove -y

# Update the software database
echo "Updating the software database..."
apt update -y

# Upgrade the entire system
echo "Upgrading the system..."
apt upgrade -y

echo "System management tasks completed successfully!"

