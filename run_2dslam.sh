echo "Start robot driver"
rosrun rosaria RosAria _port:=/dev/ttyUSB0 &

echo "Start lidar"
rosrun urg_node urg_node &

echo "Start gmapping"
roslaunch  peoplebot_slam peoplebot_gmapping.launch

