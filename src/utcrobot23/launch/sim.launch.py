import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node


def generate_launch_description():
  rviz2=Node(
    package="rviz2",
    executable='rviz2',
    arguments=['-d' + os.path.join(get_package_share_directory("utcrobot23"), 'config', 'view_bot.rviz')]
  )

  launch_sim = IncludeLaunchDescription(
    PythonLaunchDescriptionSource([os.path.join(
      get_package_share_directory('utcrobot23'), 'launch'),
      '/launch_sim.launch.py']),
      launch_arguments={'world': './src/utcrobot23/worlds/tablep23.world'}.items(),
  )

  
  launch_localization = IncludeLaunchDescription(
    PythonLaunchDescriptionSource([os.path.join(
      get_package_share_directory('utcrobot23'), 'launch'),
      '/localization_launch.py']),
      launch_arguments={'map': './src/utcrobot23/maps/table23_save.yaml',
                         'use_sim_time': 'True'}.items(),
  )
  
  # delayed_localization = TimerAction(period=10.0, actions=[launch_localization])


  # launch_navigation = IncludeLaunchDescription(
  #   PythonLaunchDescriptionSource([os.path.join(
  #     get_package_share_directory('utcrobot23'), 'launch'),
  #     '/navigation_launch.py']),
  #     launch_arguments={'use_sim_time': 'true', 'map_subscribe_transient_local': 'true'}.items(),
  # )
  # delayed_navigation = TimerAction(period=20.0, actions=[launch_navigation])




  # Launch them all!
  return LaunchDescription([
    rviz2,
    launch_sim,
    launch_localization,
    # launch_navigation,
  ])