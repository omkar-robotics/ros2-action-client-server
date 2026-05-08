import time
import rclpy

from rclpy.node import Node

from rclpy.action import ActionServer
from rclpy.action.server import ServerGoalHandle

from my_robot_interface.action import CountUntil


class CountUntilServerNode(Node):

    def __init__(self):
        super().__init__("count_until_server")

        self.count_until_server = ActionServer(
            self,
            CountUntil,
            "count_until",
            goal_callback=self.goal_callback,
            execute_callback=self.execute_callback
        )

        self.get_logger().info("Action server started")


    def goal_callback(self, goal_request):

        self.get_logger().info("Received goal")

        return rclpy.action.GoalResponse.ACCEPT


    def execute_callback(self, goal_handle: ServerGoalHandle):

        self.get_logger().info("Executing goal...")

        target_number = goal_handle.request.target_number
        delay = goal_handle.request.delay

        for i in range(target_number + 1):

            self.get_logger().info(str(i))

            time.sleep(delay)

        goal_handle.succeed()

        result = CountUntil.Result()
        result.reached_number = target_number

        return result


def main(args=None):

    rclpy.init(args=args)

    node = CountUntilServerNode()

    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
