#!/bin/bash

# Check if a directory argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

# Assign the directory path
TARGET_DIR="$1"

# Check if the provided path is a valid directory
if [ ! -d "$TARGET_DIR" ]; then
    echo "Error: $TARGET_DIR is not a valid directory."
    exit 1
fi

# Change permissions of all files and directories in the target directory
chmod -R 644 "$TARGET_DIR"

echo "Permissions for all objects in $TARGET_DIR have been changed to rw-r--r--."
