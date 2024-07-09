# moveo_ros
BNC3D Moveo ROS with manual

Original moveo ROS from https://github.com/jesseweisberg/moveo_ros?tab=readme-ov-file

Original CAD and firmware from https://github.com/BCN3D/BCN3D-Moveo

This project is designed to control a BCN3D Moveo robotic arm using ROS (Robot Operating System) and MoveIt for motion planning. The project includes custom scripts for forward kinematics and predefined movements for pick and place operations.

![image](https://github.com/reaper1947/moveo_ros/assets/153167916/80f1afe9-227f-4ee9-bfcb-4040c29500b9)

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Files and Directories](#files-and-directories)
- [Predefined Movements](#predefined-movements)
- [Known Issues](#known-issues)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Future](#future)

# Installation
Build the Workspace
```
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```
# Usage

Running the ROS Nodes

### Fisrt control with Python code
1. Start ROS Master
```
roscore
```
2. Run the MoveIt Node
```
rosrun moveo_moveit moveit_convert
```
3. Run the Serial Node
```
rosrun rosserial_python serial_node.py /dev/ttyACM0
```
4. Run the Pick and Place Script
```
rosrun moveo_moveit pick_and_place.py
```

### Secound control with terminal
after step 3 you need to run this code on terminal

1. gripper control
```
rostopic pub gripper_angle std_msgs/UInt16 <angle 0-180>
```
2. Robot control
```
rostopic pub joint_steps moveo_moveit/ArmJointState <Joint1 Joint2 Joint3 Joint4 Joint5 0>
```
also you can see a ```joint_steps``` on terminal real time by this code
```rostopic echo /<topic> ```

![image](https://github.com/reaper1947/moveo_ros/assets/153167916/e7f0aeef-cd5d-40c6-84af-5ec9fcfba654)

### Controlling the Arm
You can control the arm using predefined movements for picking and placing objects by entering commands when prompted.

# Files and Directories
- src/moveo_moveit/scripts/
   - ```pick_and_place.py```: Script for controlling the arm to perform pick and place operations.
- urdf/: Contains the URDF model of the BCN3D Moveo.
- launch/: Launch files for starting the MoveIt and ROS nodes.

# Predefined Movements
Predefined movements for picking and placing objects are defined in pick_and_place.py. The script includes trajectories for objects like a box and a cylinder.
```
box_pick = [4000, 2500, 18000, 0, 0, gripper['box']]
cylinder_pick = [5000, 2300, 20000, 0, 0, gripper['cylinder']]
# More movements...
```

![image](https://github.com/reaper1947/moveo_ros/assets/153167916/5d423347-b76c-4833-88ae-934b7c0e3c92)


# Known Issues
- [ WARN] [xxxx]: Kinematics solver doesn't support #attempts anymore, but only a timeout.
   To fix this, remove the kinematics_solver_attempts parameter from your configuration.

# Troubleshooting
### Common Errors
```Lost sync with device, restarting...```
Check the connection to the device and ensure it is properly powered.

```termios.error: (5, 'Input/output error')```
Ensure that the correct serial port is specified and the device is properly connected.

If you can't run any file when you ```roscore```  you need to use this code to make your path for ROS 

```
export ROS_PACKAGE_PATH=/home/ter/catkin_ws/src:/opt/ros/melodic/share:/home/ter/catkin_ws/src_
```
# Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes.

# Prerequisites
## Software
- Ubuntu 18.04
- ROS Melodic
- Python 2.7 and Python 3
- arduino IDE
- [MoveIt](https://moveit.ros.org/install/)
- Git
## Hardware
![image](https://github.com/reaper1947/moveo_ros/assets/153167916/8f491073-500d-4af6-8019-c860c7393b15)
![image](https://github.com/reaper1947/moveo_ros/assets/153167916/0737fff3-5d8c-4ab7-93af-9878418b8ea1)


# Clone the Repository
```
git clone https://github.com/reaper1947/moveo_ros.git
cd moveo_ros
```

![image](https://github.com/reaper1947/moveo_ros/assets/153167916/d577cbeb-763a-4ba6-a9c9-0c0fbd9e5291)


# Future
Now I'm developing ROS2 with functions that are more suitable for use in real environments, such as on AMR robots.
