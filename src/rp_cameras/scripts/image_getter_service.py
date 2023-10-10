#!/usr/bin/env python3

import rospy
from cv_bridge import CvBridge, CvBridgeError
import message_filters
from sensor_msgs.msg import Image, PointCloud, CameraInfo
import cv2
import numpy as np
from copy import deepcopy
import time

from geometry_msgs.msg import Point, Pose, PoseArray
import std_msgs.msg
import rp_cameras_msgs.srv

# Adjust these topic names according to your ZED 2i ROS topic names
input_color_img_topic = "/ee_camera/zed2i/rgb/image_rect_color"
input_depth_img_topic = "/ee_camera/zed2i/depth/depth_registered"

curr_rgb = None
curr_depth = None

def service_publisher(devnull):
    for i in range(5):
        rospy.loginfo("Publish:{}".format(i))
        rgbpub.publish(curr_rgb)
        depthpub.publish(curr_depth)
        rospy.sleep(0.1)
    return (curr_rgb, curr_depth)

def img_data_callback(input_color_img_msg, input_depth_img_msg):
    global curr_depth
    global curr_rgb
    curr_rgb = input_color_img_msg
    curr_depth = input_depth_img_msg

def img_sender_srv(devnull):
    return (curr_rgb, curr_depth)

rospy.init_node("ImageGetterService")
input_color_img_sub = message_filters.Subscriber(input_color_img_topic, Image)
input_depth_img_sub = message_filters.Subscriber(input_depth_img_topic, Image)
ts = message_filters.ApproximateTimeSynchronizer([input_color_img_sub, input_depth_img_sub], 20, 0.03)
ts.registerCallback(img_data_callback)

pose_service = rospy.Service('/Images/get_image', rp_cameras_msgs.srv.GetPairImages, img_sender_srv)
pub_service = rospy.Service('/Images/publish_images', rp_cameras_msgs.srv.GetPairImages, service_publisher)

rgbpub = rospy.Publisher("/Images/rgb", Image)
depthpub = rospy.Publisher("/Images/depth", Image)

rate = rospy.Rate(5)
while not rospy.is_shutdown():
    rate.sleep()

