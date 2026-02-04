from setuptools import find_packages, setup

package_name = 'robot_nodes'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gilad',
    maintainer_email='giladberkove10@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'motor_node = robot_nodes.motor_node:main',
            'state_machine = robot_nodes.state_machine:main',
            'distance_sensor = robot_nodes.distance_sensor:main',
        ],
    },
)
