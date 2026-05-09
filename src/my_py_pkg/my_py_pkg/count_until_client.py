import rclpy

from rclpy.node import Node
from rclpy.action import ActionClient
from rclpy.action.client import ClientGoalHandle

from my_robot_interface.action import CountUntil


class CountUntilClientNode(Node):

    def __init__(self):
        super().__init__("count_until_client")

        self.count_until_client_ = ActionClient(
            self,
            CountUntil,
            "count_until"
        )

    def send_goal(self, target_number, delay):

        self.count_until_client_.wait_for_server()

        goal = CountUntil.Goal()

        goal.target_number = target_number
        goal.delay = delay

        self.count_until_client_.send_goal_async(
            goal,
            feedback_callback=self.goal_feedback_callback
        ).add_done_callback(self.goal_response_callback)

    # Goal response callback
    def goal_response_callback(self, future):

        goal_handle: ClientGoalHandle = future.result()

        if goal_handle.accepted:
            self.get_logger().info("Goal accepted")

            goal_handle.get_result_async().add_done_callback(
                self.goal_result_callback
            )

        else:
            self.get_logger().warn("Goal rejected")

    # Feedback callback
    def goal_feedback_callback(self, feedback_msg):

        number = feedback_msg.feedback.current_number

        self.get_logger().info(
            f"Current Number: {number}"
        )

    # Result callback
    def goal_result_callback(self, future):

        result = future.result().result

        self.get_logger().info(
            f"Result: {result.reached_number}"
        )

        rclpy.shutdown()


def main(args=None):

    rclpy.init(args=args)

    node = CountUntilClientNode()

    node.send_goal(100, 0.2)

    rclpy.spin(node)


if __name__ == "__main__":
    main()
