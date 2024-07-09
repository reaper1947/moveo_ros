#!/usr/bin/env python

import rospy
from std_msgs.msg import String

from moveo_moveit.msg import ArmJointState

def main():
    # Initialize ROS node
    rospy.init_node('arm_control_node', anonymous=True)
    
    # Create a publisher for the joint steps topic
    pub = rospy.Publisher('joint_steps', ArmJointState, queue_size=10)
    
    # Set the loop rate (Hz)
    rate = rospy.Rate(1)  # 1 Hz (adjust as needed)
    
    # Define the joint steps
    joint_steps = ArmJointState()
    joint_steps.position1 = 4500
    joint_steps.position2 = 0
    joint_steps.position3 = 0
    joint_steps.position4 = 0
    joint_steps.position5 = 0
    joint_steps.position6 = 0

    joint_steps_2 = ArmJointState()
    joint_steps_2.position1 = 0
    joint_steps_2.position2 = 0
    joint_steps_2.position3 = 0
    joint_steps_2.position4 = 0
    joint_steps_2.position5 = 0
    joint_steps_2.position6 = 0
    
    # Main loop
    while not rospy.is_shutdown():
        # Publish the joint steps
        pub.publish(joint_steps)
        
        # Sleep to maintain the loop rate
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
