#!/usr/bin/env python

import rospy
import tf
from ar_track_alvar_msgs.msg import AlvarMarkers

class ARTFRepublisher(object):
    def __init__(self):
        self.subscriber = rospy.Subscriber('/ar_pose_marker', AlvarMarkers, self.cb_ar_received)
        self.tfb = tf.TransformBroadcaster()

    def cb_ar_received(self, msg):
        for marker in msg.markers:
            print marker
            print "---"
            self.tfb.sendTransform([marker.pose.pose.position.x,
                                    marker.pose.pose.position.y,
                                    marker.pose.pose.position.z],
                                   [marker.pose.pose.orientation.x,
                                    marker.pose.pose.orientation.y,
                                    marker.pose.pose.orientation.z,
                                    marker.pose.pose.orientation.w],
                                 rospy.Time.now(), msg.header.frame_id, 'single_ar_marker')

if __name__=='__main__':
    rospy.init_node('ar_tf_republisher')
    ARTFRepublisher()
    rospy.spin()
