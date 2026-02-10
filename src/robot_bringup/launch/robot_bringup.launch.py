import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    
    # 1. Get the path to your config file
    # This looks into the 'install' folder where colcon put your YAML
    config_file_path = os.path.join(
        get_package_share_directory('robot_bringup'),
        'config',
        'robot_params.yaml'
    )
    
    motor_node = Node(
        package='robot_nodes',
        executable='motor_node',
        name='motor_node',
        parameters=[config_file_path]
    )

    brain_node = Node(
        package='robot_nodes',
        executable='state_machine',
        name='state_machine',
        parameters=[config_file_path]
    )

    sensor_node = Node(
        package='robot_sensors',
        executable='distance_sensor',
        name='distance_sensor',
        parameters=[config_file_path]
    )


    # 3. Return the description to ROS
    return LaunchDescription([
        motor_node,
        sensor_node,
        brain_node
    ])