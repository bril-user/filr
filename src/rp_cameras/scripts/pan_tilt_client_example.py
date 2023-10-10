#!/usr/bin/env python3

import sys
import rospy
from rp_cameras_msgs.srv import SetPanTiltJoints

NODE_NAME = "pan_tilt_client_example"
PAN_TILT_SERVICE_NAME = "/pan_tilt/set_pan_tilt_joints"

if __name__ == "__main__":
    rospy.init_node(NODE_NAME)
    pan = float(sys.argv[1])
    tilt = float(sys.argv[2])

    rospy.wait_for_service(PAN_TILT_SERVICE_NAME)
    try:
        setPanTiltPos = rospy.ServiceProxy(PAN_TILT_SERVICE_NAME, SetPanTiltJoints)
        response = setPanTiltPos(pan, tilt)
    except rospy.ServiceException as e:   # 使用 'as' 而不是 ','.
        print("Service call failed: "+str(e))
    else:
        print("Service responded "+str(response.response))

