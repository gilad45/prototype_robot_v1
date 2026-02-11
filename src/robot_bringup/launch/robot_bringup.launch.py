import os
import xacro
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
    bringup_dir = get_package_share_directory('robot_bringup')
    descr_dir = get_package_share_directory('robot_description')
    
    config_file_path = os.path.join(bringup_dir, 'config', 'robot_params.yaml')
    
    # Path to your xacro file
    xacro_file = os.path.join(descr_dir, 'urdf', 'robot.urdf.xacro')

    # --- 2. Process Xacro to XML ---
    robot_description_config = xacro.process_file(xacro_file).toxml()
    
    # --- 3. Define Robot State Publisher ---
    # This node takes the xacro and publishes the /robot_description topic and TFs
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_config}]
    )

    node_joint_state_publisher_gui = Node(
    package='joint_state_publisher_gui', # The package name
    executable='joint_state_publisher_gui', # The executable name (MUST have _gui)
    name='joint_state_publisher_gui',
    output='screen'
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
        robot_state_publisher,
        motor_node,
        sensor_node,
        brain_node
    ])