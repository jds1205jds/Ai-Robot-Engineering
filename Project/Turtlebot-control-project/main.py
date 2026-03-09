import sys
import rclpy
import random
import time
import math
from rclpy.node import Node
from rclpy.action import ActionClient
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from rclpy.qos import qos_profile_sensor_data
from gazebo_msgs.srv import SpawnEntity
from std_srvs.srv import Empty
from turtlebot3_msgs.action import Patrol

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer

try:
    from turtle_project.control_button_ui import Ui_MainWindow
except ImportError:
    class Ui_MainWindow:
        def setupUi(self, obj): pass

class MyRobotControl(QMainWindow, Ui_MainWindow):
    def __init__(self, ros_node):
        super().__init__()
        self.setupUi(self)
        self.node = ros_node

        self.is_navi_mode = False
        self.is_action_running = False
        self.current_x, self.current_y, self.current_yaw = 0.0, 0.0, 0.0
        self.TARGET_X, self.TARGET_Y = 2.0, 2.0

        self.manual_linear = 0.0
        self.manual_angular = 0.0

        self._action_client = ActionClient(self.node, Patrol, 'patrol')
        self.publisher = self.node.create_publisher(Twist, '/cmd_vel', 10)
        self.scan_sub = self.node.create_subscription(LaserScan, '/scan', self.scan_callback, qos_profile=qos_profile_sensor_data)
        self.odom_sub = self.node.create_subscription(Odometry, '/odom', self.odom_callback, 10)
        self.spawn_client = self.node.create_client(SpawnEntity, '/spawn_entity')
        self.reset_client = self.node.create_client(Empty, '/reset_simulation')

        self.btn_go.clicked.connect(lambda: self.set_manual_vel(0.2, 0.0))
        self.btn_back.clicked.connect(lambda: self.set_manual_vel(-0.2, 0.0))
        self.btn_left.clicked.connect(lambda: self.set_manual_vel(0.0, 0.6))
        self.btn_right.clicked.connect(lambda: self.set_manual_vel(0.0, -0.6))
        self.btn_stop.clicked.connect(self.stop_all)
        self.btn_reset.clicked.connect(self.call_reset)
        self.btn_add.clicked.connect(self.spawn_big_cone)
        self.btn_navi.clicked.connect(self.toggle_navi)
        self.btn_squre.clicked.connect(lambda: self.send_action_goal(1.0))
        self.btn_triangle.clicked.connect(lambda: self.send_action_goal(2.0))

        self.ui_update_timer = QTimer()
        self.ui_update_timer.timeout.connect(self.update_ui)
        self.ui_update_timer.start(100)

        QTimer.singleShot(2500, self.spawn_green_flag)

    def odom_callback(self, msg):
        self.current_x = msg.pose.pose.position.x
        self.current_y = msg.pose.pose.position.y
        q = msg.pose.pose.orientation
        self.current_yaw = math.atan2(2*(q.w*q.z + q.x*q.y), 1 - 2*(q.y*q.y + q.z*q.z))

    def update_ui(self):
        dist = math.sqrt((self.TARGET_X - self.current_x)**2 + (self.TARGET_Y - self.current_y)**2)
        try:
            val = int(max(0, (1.0 - (dist / 3.0))) * 100)
            if hasattr(self, 'progressBar'):
                self.progressBar.setValue(val)
        except AttributeError:
            pass

    def scan_callback(self, msg):
        if self.is_action_running: return

        # 감지 각도
        front_ranges = msg.ranges[0:20] + msg.ranges[340:360]

        # 감지 거리
        obstacles = [r for r in front_ranges if 0.1 < r < 0.25]

        if obstacles:
            self.node.get_logger().info("장애물 근접")
            # 살짝 전진(0.05)하면서 회전(0.8)
            self.send_vel(0.05, 0.8)
            return

        if self.is_navi_mode:
            dx, dy = self.TARGET_X - self.current_x, self.TARGET_Y - self.current_y
            dist = math.sqrt(dx**2 + dy**2)
            angle_to_target = math.atan2(dy, dx)
            angle_diff = math.atan2(math.sin(angle_to_target - self.current_yaw),
                                    math.cos(angle_to_target - self.current_yaw))

            if dist < 0.15:
                self.node.get_logger().info("목적지 도착!")
                self.stop_all()
            elif abs(angle_diff) > 0.15:
                self.send_vel(0.05, 0.6 if angle_diff > 0 else -0.6)
            else:
                self.send_vel(0.2, 0.0)

        elif self.manual_linear != 0.0 or self.manual_angular != 0.0:
            self.send_vel(self.manual_linear, self.manual_angular)

    def set_manual_vel(self, lx, az):
        self.is_navi_mode = False
        self.manual_linear = float(lx)
        self.manual_angular = float(az)
        self.send_vel(lx, az)

    def spawn_green_flag(self):
        if not self.spawn_client.wait_for_service(timeout_sec=1.0): return
        req = SpawnEntity.Request()
        req.name = "GREEN_FLAG"
        req.xml = f"""
        <sdf version='1.6'><model name='GREEN_FLAG'><static>true</static>
        <pose>{self.TARGET_X} {self.TARGET_Y} 0 0 0 0</pose>
        <link name='l'>
            <visual name='p'><pose>0 0 0.6 0 0 0</pose><geometry><cylinder><radius>0.03</radius><length>1.2</length></cylinder></geometry><material><ambient>0.3 0.3 0.3 1</ambient></material></visual>
            <visual name='f'><pose>0.2 0 1.05 0 0 0</pose><geometry><box><size>0.4 0.01 0.25</size></box></geometry><material><ambient>0 1 0 1</ambient><diffuse>0 1 0 1</diffuse></material></visual>
        </link></model></sdf>"""
        self.spawn_client.call_async(req)

    def spawn_big_cone(self):
        if not self.spawn_client.service_is_ready(): return
        req = SpawnEntity.Request()
        name = f"BIG_CONE_{int(time.time())}"
        d, a = random.uniform(1.2, 2.0), random.uniform(0, 2*math.pi)
        px, py = self.current_x + d*math.cos(a), self.current_y + d*math.sin(a)
        req.name = name
        req.xml = f"""
        <sdf version='1.6'><model name='{name}'><static>true</static><pose>{px} {py} 0 0 0 0</pose>
        <link name='l'>
            <collision name='c'><pose>0 0 0.2 0 0 0</pose><geometry><cylinder><radius>0.25</radius><length>0.4</length></cylinder></geometry></collision>
            <visual name='v'>
                <geometry>
                    <mesh>
                        <uri>model://construction_cone/meshes/construction_cone.dae</uri>
                        <scale>3.5 3.5 3.5</scale>  </mesh>
                </geometry>
                <material><ambient>1 0.3 0 1</ambient><diffuse>1 0.3 0 1</diffuse></material>
            </visual>
        </link></model></sdf>"""
        self.spawn_client.call_async(req)

    def toggle_navi(self):
        self.manual_linear = 0.0
        self.manual_angular = 0.0
        self.is_navi_mode = True
        self.node.get_logger().info("내비게이션 활성화")

    def send_action_goal(self, mode):
        if not self._action_client.wait_for_server(timeout_sec=1.0): return
        self.stop_all()
        self.is_action_running = True
        goal_msg = Patrol.Goal()
        goal_msg.goal.x = float(mode)
        self._action_client.send_goal_async(goal_msg).add_done_callback(
            lambda f: f.result().get_result_async().add_done_callback(lambda _: setattr(self, 'is_action_running', False)))

    def send_vel(self, lx, az):
        msg = Twist()
        msg.linear.x, msg.angular.z = float(lx), float(az)
        self.publisher.publish(msg)

    def stop_all(self):
        self.is_navi_mode = False
        self.is_action_running = False
        self.manual_linear = 0.0
        self.manual_angular = 0.0
        self.send_vel(0.0, 0.0)

    def call_reset(self):
        if self.reset_client.service_is_ready():
            self.reset_client.call_async(Empty.Request())
            self.stop_all()
            QTimer.singleShot(1000, self.spawn_green_flag)

def main(args=None):
    rclpy.init(args=args)
    node = Node('TURTLE_CONTROL_NODE')
    app = QApplication(sys.argv)
    gui = MyRobotControl(node)
    gui.show()
    timer = QTimer()
    timer.timeout.connect(lambda: rclpy.spin_once(node, timeout_sec=0))
    timer.start(10)
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
