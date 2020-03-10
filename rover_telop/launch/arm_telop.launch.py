import launch
import launch_ros.actions
import launch.actions


def generate_launch_description():
	return launch.LaunchDescription([
		launch_ros.actions.Node(
			package='joy', node_executable='joy_node', arguments=["_dev_name:=", "Microsoft X-Box One S pad", "_deadzone:=", "0.12", "_coalesce_interval:=", "0.1"], remappings=["joy_arm", "joy"], output='screen')
	])