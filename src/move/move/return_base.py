from move.utils import create_pose
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
from rclpy.duration import Duration

def return_base(initial_pose: dict, navigator: BasicNavigator):
    """
    Initial pose contains key position and rotation.
    """

    navigator.waitUntilNav2Active()

    start = create_pose(initial_pose)
        
    navigator.goToPose(start)

    i = 0
    while not navigator.isTaskComplete():

        # Do something with the feedback
        i = i + 1
        feedback = navigator.getFeedback()
        if feedback and i % 5 == 0:
            print('Estimated time of arrival to initial pose: ' + '{0:.0f}'.format(
                Duration.from_msg(feedback.estimated_time_remaining).nanoseconds / 1e9)
                + ' seconds.')

    # Do something depending on the return code
    result = navigator.getResult()
    if result == TaskResult.SUCCEEDED:
        print('Initial Pose!')
    elif result == TaskResult.CANCELED:
        print('Goal was canceled!')
    elif result == TaskResult.FAILED:
        print('Goal failed!')
    else:
        print('Goal has an invalid return status!')