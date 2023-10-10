#!/usr/bin/env python3




import rospy
import time
import math
from rp_cameras_msgs.srv import SetPanTiltJoints,SetPanTiltJointsResponse
from sensor_msgs.msg import JointState


PAN_TILT_SERVER_NAME = "pan_tilt_server_node"
PAN_TILT_SERVICE_NAME = "set_pan_tilt_joints"
PTU_CONTROL_TOPIC = "cmd"


#from flir PTU-E46 user manual 1.00
FACTORY_PAN_MIN = -159.0/180.0*math.pi
FACTORY_PAN_MAX =  159.0/180.0*math.pi
FACTORY_TILT_MIN = -47.0/180.0*math.pi
FACTORY_TILT_MAX =  31.0/180.0*math.pi



ptu_control_msg_publisher = None
pan_joint_velocity = 0.6
tilt_joint_velocity = 0.6


def handleRequest(req):
    """Handles a pan tilt movement request

    Parameters
    ----------
    req : SetPanTiltJoints
        SetPanTiltJoints message defining the pose to get to

    Returns
    -------
    SetPanTiltJointsResponse
        Result of the service request, see the service definition in the SetPanTiltJoints.srv file

    """
    pan = req.pan
    tilt = req.tilt

    if math.isnan(pan) or math.isinf(pan):
        rospy.logerr("Received invalid pan angle "+str(pan))
        return SetPanTiltJointsResponse(SetPanTiltJointsResponse.INVALID_INPUT)
    if math.isnan(tilt) or math.isinf(tilt):
        rospy.logerr("Received invalid tilt angle "+str(tilt))
        return SetPanTiltJointsResponse(SetPanTiltJointsResponse.INVALID_INPUT)

    if pan<FACTORY_PAN_MIN or FACTORY_PAN_MAX<pan:
        rospy.logerr("Received pan angle out of factory limit. Pan="+str(pan)+" limits=["+str(FACTORY_PAN_MIN)+";"+str(FACTORY_PAN_MAX)+"]")
        return SetPanTiltJointsResponse(SetPanTiltJointsResponse.OUT_OF_RANGE)
    if tilt<FACTORY_TILT_MIN or FACTORY_TILT_MAX<tilt:
        rospy.logerr("Received tilt angle out of factory limit. Tilt="+str(tilt)+" limits=["+str(FACTORY_TILT_MIN)+";"+str(FACTORY_TILT_MAX)+"]")
        return SetPanTiltJointsResponse(SetPanTiltJointsResponse.OUT_OF_RANGE)



    js = JointState()
    js.name = [ "ptu_pan", "ptu_tilt" ]
    js.velocity = [ pan_joint_velocity, tilt_joint_velocity ]
    js.position = [ pan, tilt ]
    ptu_control_msg_publisher.publish(js)

    return SetPanTiltJointsResponse(SetPanTiltJointsResponse.SUCCESS)

if __name__ == "__main__":
    rospy.init_node(PAN_TILT_SERVER_NAME)
    ptu_control_msg_publisher = rospy.Publisher(PTU_CONTROL_TOPIC, JointState, queue_size=1)
    time.sleep(0.5) # ugly, but effective

    s = rospy.Service(PAN_TILT_SERVICE_NAME, SetPanTiltJoints, handleRequest)
    print("Service "+str(PAN_TILT_SERVICE_NAME)+" started")
    rospy.spin()
