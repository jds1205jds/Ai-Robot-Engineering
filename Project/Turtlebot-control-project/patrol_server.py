import time
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from geometry_msgs.msg import Twist
from turtlebot3_msgs.action import Patrol

class PatrolServer(Node):
    def __init__(self):
        super().__init__('patrol_server')

        self._action_server = ActionServer(
            self,
            Patrol,
            'patrol',
            self.execute_callback
        )


        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.get_logger().info('액션 서버가 시작되었습니다!')

    async def execute_callback(self, goal_handle):
        self.get_logger().info('주행')

        # x=1.0 이면 네모, x=2.0 이면 세모
        mode = goal_handle.request.goal.x
        sides = 4 if mode == 1.0 else 3

        feedback_msg = Patrol.Feedback()
        result = Patrol.Result()

        for i in range(sides):
            # 전진
            self.move_robot(0.2, 0.0, 2.0)

            # 회전
            turn_time = 1.85 if sides == 4 else 2.45
            self.move_robot(0.0, 0.8, turn_time)

            # 피드백 보내기
            feedback_msg.state = f"{i+1}번째 변 주행 중"
            goal_handle.publish_feedback(feedback_msg)

        goal_handle.succeed()
        result.result = "Success"
        self.get_logger().info('주행 완료!')
        return result

    def move_robot(self, linear, angular, duration):
        """특정 시간 동안 로봇을 움직이는 보조 함수"""
        twist = Twist()
        twist.linear.x = linear
        twist.angular.z = angular

        start_time = time.time()
        while time.time() - start_time < duration:
            self.publisher.publish(twist)
            time.sleep(0.1)

        # 정지
        twist.linear.x = 0.0
        twist.angular.z = 0.0
        self.publisher.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = PatrolServer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
