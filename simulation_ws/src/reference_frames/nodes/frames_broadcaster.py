#!/usr/bin/env python
import rospy
import tf

# Constant definitions
L3 = 1.6

if __name__ == '__main__':
    rospy.init_node("end_effector_position")
    br = tf.TransformBroadcaster()
    listener = tf.TransformListener()
    rate = rospy.Rate(10.0)

    while not rospy.is_shutdown():
        br.sendTransform((0.0, 0.0, L3),
                         (0.0, 0.0, 0.0, 1.0),
                         rospy.Time.now(),
                         "end_effector", "link3")
        try:
            (trans, rot) = listener.lookupTransform('/world', 'end_effector', rospy.Time(0))
            print(trans)
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        rate.sleep()
