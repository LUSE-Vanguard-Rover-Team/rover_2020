#!/bin/bash
sudo updatedb
working_dir=$(locate -b rover_2020)

echo "Installing ROS 2"
sudo apt update && sudo apt install curl gnupg2 lsb-release -y
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
sudo sh -c 'echo "deb [arch=amd64,arm64] http://packages.ros.org/ros2/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/ros2-latest.list'
sudo apt update
sudo apt install ros-eloquent-desktop -y
sudo apt install python3-argcomplete -y
source /opt/ros/eloquent/setup.bash
echo "source /opt/ros/eloquent/setup.bash" >> ~/.bashrc
echo "export ROS_DOMAIN_ID=1" >> ~/.bashrc
sudo apt install python3-colcon-common-extensions -y
printenv | grep -i ROS
echo ""
echo ""

echo "Setting up workspace"
sleep 2
cd $working_dir/ros2ws
colcon build
echo "source $working_dir/ros2ws/install/setup.bash" >> ~/.bashrc
source $working_dir/ros2ws/install/setup.bash
echo "Finished setup"
