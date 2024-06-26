import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node

def generate_launch_description():

    ####### Input your URDF FILE ##########
    xacro_file = 'robot.urdf.xacro'
    package_description = "rabbit_description" # Package name where urdf file is present

    print("Fetching URDF ==>")
    robot_desc_path = os.path.join(get_package_share_directory(package_description), "urdf", xacro_file)

    # Robot State Publisher Node 
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher_node',
        emulate_tty=True,
        parameters=[{'use_sim_time': True, 'robot_description': Command(['xacro ', robot_desc_path])}],
        output="screen"
    )

    rviz_config_file = os.path.join(get_package_share_directory(package_description), 'rviz', 'rviz_config.rviz')
    
    rviz2_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2_node',
        output='screen',
        arguments=['-d', rviz_config_file]
    )

    # Create and return launch description object
    return LaunchDescription(
        [            
            robot_state_publisher_node,
            rviz2_node
        ]
    )
