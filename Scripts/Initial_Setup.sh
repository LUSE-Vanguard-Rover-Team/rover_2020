#!/bin/bash
working_dir=$(locate -b rover_2020)

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
sudo apt install python3-colcon-common-extensions
printenv | grep -i ROS
sleep 2

echo "Setting up workspace"
cd $working_dir/ros2ws
colcon build
echo "source $working_dir/ros2ws/install/setup.bash" >> ~/.bashrc
echo "Finished setup"
