import launch
import launch_ros.actions
import launch.actions


def generate_launch_description():
	return launch.LaunchDescription([
		launch_ros.actions.Node(
			package='rover_telop', node_executable='drive_telop', output='screen'),
		launch_ros.actions.Node(
			package='joy', node_executable='joy_node', arguments=["dev_name:=", "*", "deadzone:=", "0.12"], output='screen')
	])