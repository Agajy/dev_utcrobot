from setuptools import setup
import os
from glob import glob

package_name = 'move'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lgontier',
    maintainer_email='lucas.gontier@etu.utc.fr',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'move_to_pose = move.move_to_pose:main',
            'set_initial_pose = move.set_initial_pose:main',
            'follow_waypoints = move.follow_waypoints:main'
        ],
    },
)
