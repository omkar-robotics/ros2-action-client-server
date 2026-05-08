import rclpy

from rclpy.node import Node

from rclpy.action import ActionClient

from my_robot_interface.action import CountUntil


class CountUntilClientNode(Node):

    def __init__(self):
        super().__init__("count_until_client")

        self.count_until_client = ActionClient(
            self,
            CountUntil,
            "count_until"
        )


    def send_goal(self, target_number, delay):

        self.count_until_client.wait_for_server()

        goal = CountUntil.Goal()

        goal.target_number = target_number
        goal.delay = delay

        self.get_logger().info("Sending goal...")

        self.count_until_client.send_goal_async(
            goal
        ).add_done_callback(self.goal_response_callback)


    def goal_response_callback(self, future):

        goal_handle = future.result()

        if not goal_handle.accepted:
            self.get_logger().info("Goal rejected")
            return

        self.get_logger().info("Goal accepted")

        goal_handle.get_result_async().add_done_callback(
            self.get_result_callback
        )


    def get_result_callback(self, future):

        result = future.result().result

        self.get_logger().info(
            "Result: " + str(result.reached_number)
        )

        rclpy.shutdown()


def main(args=None):

    rclpy.init(args=args)

    node = CountUntilClientNode()

    node.send_goal(100, 1.0)

    rclpy.spin(node)


if __name__ == "__main__":
    main()
