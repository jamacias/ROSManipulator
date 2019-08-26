#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64

def joint_states_callback(message):
    rospy.loginfo("Joint coordinates [rad] %s", message.position) # [q1, q2, q3]
    rospy.loginfo("Joint velocities [rad/s] %s", message.velocity) # [q1, q2, q3]
    rospy.loginfo("Joint efforts [Nm] %s", message.effort) # [q1, q2, q3]

if __name__ == '__main__':
    rospy.init_node("joint_space")
    rospy.Subscriber("joint_states", JointState, joint_states_callback, queue_size=1)
    rospy.spin()
