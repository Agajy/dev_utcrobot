from geometry_msgs.msg import PoseWithCovariance
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
from rclpy.duration import Duration
import sys
from move.utils import create_pose
from move.return_base import return_base

import json

"""
Basic navigation demo to go to poses.
"""


def main():
    rclpy.init()
    navigator = BasicNavigator()

    nav_start = navigator.get_clock().now()

    json_file = sys.argv[1]
    with open(json_file) as f:
        params = json.load(f)

    

    # Activate navigation, if not autostarted. This should be called after setInitialPose()
    # or this will initialize at the origin of the map and update the costmap with bogus readings.
    # If autostart, you should `waitUntilNav2Active()` instead.
    # navigator.lifecycleStartup()

    # Wait for navigation to fully activate, since autostarting nav2
    navigator.waitUntilNav2Active()

    # If desired, you can change or load the map as well
    # navigator.changeMap('/path/to/map.yaml')

    # You may use the navigator to clear or obtain costmaps
    # navigator.clearAllCostmaps()  # also have clearLocalCostmap() and clearGlobalCostmap()
    # global_costmap = navigator.getGlobalCostmap()
    # local_costmap = navigator.getLocalCostmap()

    # Set all goal poses
    goal_poses = []
    for position in params['goalPosition']:
        goal_pose_i = create_pose(position)
        goal_pose_i.header.frame_id = 'map'
        goal_pose_i.header.stamp = navigator.get_clock().now().to_msg()
        goal_poses.append(goal_pose_i)

    # sanity check a valid path exists
    # path = navigator.getPath(initial_pose, goal_pose1)

    navigator.followWaypoints(goal_poses)

    i = 0
    print(params["timeLimit"])
    while not navigator.isTaskComplete():

        # Do something with the feedback
        i = i + 1
        feedback = navigator.getFeedback()
        if feedback and i % 5 == 0:
            print('Executing current waypoint: ' +
                  str(feedback.current_waypoint + 1) + '/' + str(len(goal_poses)))
            now = navigator.get_clock().now()

            # Some navigation timeout to demo cancellation
            if now - nav_start > Duration(seconds=params["timeLimit"]):
                navigator.cancelTask()

    # Do something depending on the return code
    result = navigator.getResult()
    if result == TaskResult.SUCCEEDED:
        print('Goal succeeded!')
    elif result == TaskResult.CANCELED:
        print('Goal was canceled!')
    elif result == TaskResult.FAILED:
        print('Goal failed!')
    else:
        print('Goal has an invalid return status!')

    return_base(params['initialPosition'], navigator)


    navigator.lifecycleShutdown()

    exit(0)


if __name__ == '__main__':
    main()
