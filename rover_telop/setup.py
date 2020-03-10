import os
from glob import glob
from setuptools import setup

package_name = 'rover_telop'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Sean DeBarr',
    maintainer_email='sedebarr@liberty.edu',
    description='The rover teleoperation packages',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'drive_telop = rover_telop.joy_telop:main',
        ],
    },
)
