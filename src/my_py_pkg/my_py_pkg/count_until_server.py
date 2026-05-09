import rclpy
import time

from rclpy.node import Node

from rclpy.action import (
    ActionServer,
    GoalResponse,
    CancelResponse
)

from rclpy.action.server import ServerGoalHandle

from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import ReentrantCallbackGroup

from my_robot_interface.action import CountUntil


class CountUntilServerNode(Node):

    def __init__(self):

        super().__init__("count_until_server")

        self.count_until_server_ = ActionServer(
            self,
            CountUntil,
            "count_until",

            goal_callback=self.goal_callback,

            execute_callback=self.execute_callback,

            cancel_callback=self.cancel_callback,

            callback_group=ReentrantCallbackGroup()
        )

        self.get_logger().info(
            "Action Server Started"
        )

    # ==========================================
    # GOAL CALLBACK
    # ==========================================

    def goal_callback(self, goal_request):

        self.get_logger().info(
            "Received goal request"
        )

        self.get_logger().info(
            f"Target Number: {goal_request.target_number}"
        )

        self.get_logger().info(
            f"Delay: {goal_request.delay}"
        )

        return GoalResponse.ACCEPT

    # ==========================================
    # CANCEL CALLBACK
    # ==========================================

    def cancel_callback(self, goal_handle):

        self.get_logger().info(
            "Received cancel request"
        )

        return CancelResponse.ACCEPT

    # ==========================================
    # EXECUTE CALLBACK
    # ==========================================

    def execute_callback(
        self,
        goal_handle: ServerGoalHandle
    ):

        self.get_logger().info(
            "Executing goal..."
        )

        # Create Result object
        result = CountUntil.Result()

        # Create Feedback object
        feedback = CountUntil.Feedback()

        target_number = goal_handle.request.target_number

        delay = goal_handle.request.delay

        counter = 0

        while counter < target_number:

            # ==========================
            # CHECK CANCEL REQUEST
            # ==========================

            if goal_handle.is_cancel_requested:

                self.get_logger().info(
                    "Canceling goal..."
                )

                goal_handle.canceled()

                result.reached_number = counter

                return result

            # ==========================
            # COUNTING
            # ==========================

            counter += 1

            self.get_logger().info(
                f"Counting: {counter}"
            )

            # Fill feedback
            feedback.current_number = counter

            # Publish feedback
            goal_handle.publish_feedback(
                feedback
            )

            time.sleep(delay)

        # ==========================
        # GOAL SUCCESS
        # ==========================

        goal_handle.succeed()

        result.reached_number = counter

        self.get_logger().info(
            f"Goal completed. Result: {counter}"
        )

        return result


# ==========================================
# MAIN
# ==========================================

def main(args=None):

    rclpy.init(args=args)

    node = CountUntilServerNode()

    executor = MultiThreadedExecutor()

    rclpy.spin(
        node,
        executor
    )

    rclpy.shutdown()


if __name__ == "__main__":
    main()
