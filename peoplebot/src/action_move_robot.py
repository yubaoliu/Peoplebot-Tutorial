#! /usr/bin/env python
from actionlib_msgs.msg import GoalStatus
from geometry_msgs.msg import Pose, PoseStamped
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
import rospy
import math
import roslib
roslib.load_manifest('peoplebot')


def getPose(x, y, theta):
    pose = Pose()
    pose.position.x = x
    pose.position.y = y
    pose.orientation.z = math.sin(theta/2)
    pose.orientation.w = math.cos(theta/2)
    return pose


if __name__ == '__main__':
    rospy.init_node('Move2Waypoint')
    print("Move robot to a specific position")
    cli = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
    cli.wait_for_server()
    print("Connected to the movebase server")

    goal = PoseStamped()
    goal.header.stamp = rospy.Time.now()
    goal.header.frame_id = "map"
    goal.pose = getPose(1, 0, 0)

    send_goal = MoveBaseGoal()
    send_goal.target_pose = goal

    cli.send_goal(send_goal)
    rospy.loginfo("[Action move_base/goal] sent goal.")
    cli.wait_for_result()
    if cli.get_state() == GoalStatus.SUCCEEDED:
        rospy.loginfo("[Action move_base/goal] succeeded.")
    else:
        rospy.loginfo("[Action move_base/goal] failed.")
        cli.cancel_all_goals()

    # goal = DoDishesGoal()
    # Fill in the goal here
    # client.send_goal(goal)
    # client.wait_for_result(rospy.Duration.from_sec(5.0))
