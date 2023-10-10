#!/bin/bash

#move to scripts's directory
cd $(dirname "$0")

echo "Setting up udev rule for serial-usb adapter..."
sudo cp ./50-FT-232.rules /etc/udev/rules.d/50-FT232.rules

echo "Restarting udev service..."
sudo udevadm control --reload

echo "All good, shouldn't need a reboot (but maybe it does)"
