from turtle_tf2_py.turtle_tf2_broadcaster import quaternion_from_euler
from geometry_msgs.msg import PoseStamped


def create_pose(position: dict):
    """
    Create position.

    Params:
    - position (dict): dict have 2 keys ("position" and "rotation").
    Each key have 3 subkeys ("x", "y" and "z")
    """
    pose = PoseStamped()

    # get quaternion rotation
    quat = quaternion_from_euler(
        position["rotation"]["x"], 
        position["rotation"]["y"], 
        position['rotation']['z'])
    pose.pose.position.x = float(position['position']['x'])
    pose.pose.position.y = float(position['position']['y'])
    pose.pose.position.z = float(position['position']['z'])
    pose.pose.orientation.x = float(quat[0])
    pose.pose.orientation.y = float(quat[1])
    pose.pose.orientation.z = float(quat[2])
    pose.pose.orientation.w = float(quat[3])

    return pose