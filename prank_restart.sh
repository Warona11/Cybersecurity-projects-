#!/bin/bash
# Check if today is Friday the 13th
if [[ $(date +%u) -eq 5 && $(date +%d) -eq 13 ]]; then
    /bin/systemctl reboot
fi
