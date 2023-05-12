from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
import sys
import json 
from move.utils import create_pose

def main():
    rclpy.init()

    json_file = sys.argv[1]
    with open(json_file) as f:
        params = json.load(f)

    initial_position = params["initialPosition"]

    navigator = BasicNavigator()
    navigator.waitUntilNav2Active()

    # Set initial pose
    initial_pose = create_pose(initial_position)
    initial_pose.header.frame_id = 'map'
    initial_pose.header.stamp = navigator.get_clock().now().to_msg()
    navigator.setInitialPose(initial_pose)

    navigator.waitUntilNav2Active()

if __name__ == "__main__":
    main()