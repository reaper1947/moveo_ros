#!/usr/bin/env python
#!/usr/bin/env python3



import rospy
from std_msgs.msg import String
import sys
import zmq
# import espeak
from msgpack import loads
import time
from datetime import datetime 
from moveo_moveit.msg import ArmJointState

fixated_object_label = None
gripper = {'open': 0, 'box': 90, 'cylinder': 100}
upright = [0, 0, 0, 0, 0, 0]

#predefined movements for pick and place of an apple and banana
box_pick = [3500, 2500, 17000, 0, 500, gripper['box']]
box_pickPre = [3500, 2520, 18000, 0, 0, gripper['open']]
box_stand = [3500, 1800, 18000, 0, 0, gripper['box']]
box_move = [1000, 1800, 18000, 0, 0, gripper['box']]
box_place = [1000, 2600, 17000, 0, 0, gripper['open']]
box_stand2 = [1000, 2000, 17000, 0, 0, gripper['open']]

box_standhalf = [4500, 1800, 18000, 0, 0, gripper['open']]

cylinder_pick = [5000, 2300, 18000, 0, 1000, gripper['cylinder']]
cylinder_pickPre = [5000, 2300, 20000, 0, 0, gripper['open']]
cylinder_stand = [5000, 1800, 20000, 0, 0, gripper['cylinder']]
cylinder_move = [7500, 1800, 20000, 0, 0, gripper['cylinder']]
cylinder_place = [7500, 2300, 20000, 0, 0, gripper['open']]

# moveall_pick = [4500, 2300, 18000, 0, 0, gripper['box']]
# moveall_stand = [4500, 1800, 18000, 0, 0, gripper['box']]
# moveall_move = [1000, 1800, 18000, 0, 0, gripper['box']]
# moveall_place = [1000, 2300, 17000, 0, 0, gripper['open']]
# moveall2_pick = [4500, 2300, 18000, 0, 0, gripper['cylinder']]
# moveall2_stand = [4500, 1800, 18000, 0, 0, gripper['cylinder']]
# moveall2_move = [7500, 1800, 18000, 0, 0, gripper['cylinder']]
# moveall2_place = [7500, 2300, 17000, 0, 0, gripper['open']]

object_trajectories = {"box": [upright, box_standhalf,box_pickPre, box_pick, box_stand,  box_move, box_place,box_stand2,  box_standhalf, upright],
                      "cylinder": [upright, box_standhalf, cylinder_pickPre,cylinder_pick, cylinder_stand, cylinder_move, cylinder_place,box_standhalf, upright],
                      "moveall": [upright, box_standhalf,box_pickPre, box_pick, box_stand,  box_move, box_place, box_stand2,  box_standhalf, cylinder_pickPre,cylinder_pick, cylinder_stand, cylinder_move, cylinder_place, upright],}


# publish detected object to a ros topic
def publish_detected_object(command):
    pub = rospy.Publisher('joint_steps', ArmJointState, queue_size=4)
    rospy.init_node('pick_and_place_object_detection', anonymous=True)
    rate = rospy.Rate(20) # 20hz

    while not rospy.is_shutdown():
        if command == 1:
            fixated_object_label = 'box'
        elif command == 2:
            fixated_object_label = 'cylinder'
        elif command == 3:
            fixated_object_label = 'moveall'
        else:
            fixated_object_label = None

        rospy.loginfo(fixated_object_label)
        
        # check if fixated object label is a key in object_trajectories
        # if so, publish each trajectory in object_trajectories[key] to ArmJointState
        if fixated_object_label in object_trajectories:
            for i in object_trajectories[fixated_object_label]:
                goal = ArmJointState()
                goal.position1 = i[0]
                goal.position2 = i[1]
                goal.position3 = i[2]
                goal.position4 = i[3]
                goal.position5 = i[4]
                goal.position6 = i[5]
                pub.publish(goal)
                rospy.sleep(5)
                
        while espeak.is_playing():
             pass

        rate.sleep()
    

if __name__ == '__main__':
    while True:
        try:
            command = int(input("Enter command (1 or 2 or 3): "))
            publish_detected_object(command)
        except ValueError:
            print("Invalid input. Please enter 1, 2, or 3.")
        except rospy.ROSInterruptException:
            pass
         