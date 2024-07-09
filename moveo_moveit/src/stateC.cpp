#include "ros/ros.h"
#include "sensor_msgs/JointState.h"
#include "moveo_moveit/ArmJointState.h"
#include "math.h"


//enum State {
//    IDLE,
//    MOVE_TO_POSITION_1,
//    MOVE_TO_POSITION_2,
//    MOVE_TO_POSITION_3
//};

// Initialize the state machine state
State current_state = IDLE;

moveo_moveit::ArmJointState arm_steps;
moveo_moveit::ArmJointState total;
int stepsPerRevolution[6] = { 7500,3000,18000,800,3000,0 };  // microsteps/revolution (using 16ths) from observation, for each motor
int joint_status = 0;
double cur_angle[6];
int joint_step[6];
double prev_angle[6] = { 0,0,0,0,0,0 };
double init_angle[6] = { 0,0,0,0,0,0 };
double total_steps[6] = { 0,0,0,0,0,0 };
int count = 0;


void cmd_cb(const sensor_msgs::JointState& cmd_arm)
{
    // Your callback function remains unchanged
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "moveo_moveit");
    ros::NodeHandle nh;

    // Subscribe to the joint states topic
    ros::Subscriber sub = nh.subscribe("/move_group/fake_controller_joint_states", 1000, cmd_cb);

    // Create a publisher for the joint steps topic
    ros::Publisher pub = nh.advertise<moveo_moveit::ArmJointState>("joint_steps", 50);

    ros::Rate loop_rate(20);

    while (ros::ok())
    {
        switch (current_state)
        {
        case IDLE:
            // In IDLE state, the arm does nothing until a command is received
            break;

        case MOVE_TO_POSITION_1:
            // Set the joint positions for moving to position 1
            // Assuming you have defined the joint angles for position 1
            arm_steps.position1 = 0; // Joint 1 position for position 1
            arm_steps.position2 = 0; // Joint 2 position for position 1
            arm_steps.position3 = 0; // Joint 3 position for position 1
            arm_steps.position4 = 0; // Joint 4 position for position 1
            arm_steps.position5 = 0; // Joint 5 position for position 1
            arm_steps.position6 = 0; // Joint 6 position for position 1
            break;

        case MOVE_TO_POSITION_2:
            // Set the joint positions for moving to position 2
            // Assuming you have defined the joint angles for position 2
            arm_steps.position1 = 1000; // Joint 1 position for position 2
            arm_steps.position2 = 0; // Joint 2 position for position 2
            arm_steps.position3 = 0; // Joint 3 position for position 2
            arm_steps.position4 = 0; // Joint 4 position for position 2
            arm_steps.position5 = 0; // Joint 5 position for position 2
            arm_steps.position6 = 0; // Joint 6 position for position 2
            break;

        case MOVE_TO_POSITION_3:
            // Set the joint positions for moving to position 3
            // Assuming you have defined the joint angles for position 3
            arm_steps.position1 = 2000; // Joint 1 position for position 3
            arm_steps.position2 = 0; // Joint 2 position for position 3
            arm_steps.position3 = 0; // Joint 3 position for position 3
            arm_steps.position4 = 0; // Joint 4 position for position 3
            arm_steps.position5 = 0; // Joint 5 position for position 3
            arm_steps.position6 = 0; // Joint 6 position for position 3
            break;
        }

        // Publish the joint steps
        pub.publish(arm_steps);

        ros::spinOnce();
        loop_rate.sleep();
    }

    return 0;
}
