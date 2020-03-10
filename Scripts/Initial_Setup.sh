#!/bin/bash

echo "Installing ROS 2"
sudo apt update && sudo apt install curl gnupg2 lsb-release
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
sudo sh -c 'echo "deb [arch=amd64,arm64] http://packages.ros.org/ros2/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/ros2-latest.list'
sudo apt update
sudo apt install ros-eloquent-desktop
sudo apt install python3-argcomplete
source /opt/ros/eloquent/setup.bash
echo "source /opt/ros/eloquent/setup.bash" >> ~/.bashrc
echo "export ROS_DOMAIN_ID=1" >> ~/.bashrc
printenv | grep -i ROS
sudo apt install python3-colcon-common-extensions

echo "Setting up ROS 2 workspace!"
mkdir dev_ws
mkdir dev_ws/src
cd dev_ws/src
git clone https://github.com/LUSE-Vanguard-Rover-Team/rover_2020.git
colcon build
echo "source /Vanguard/dev_ws/src/install/setup.bash" >> ~/.bashrc
