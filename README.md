# ROS2 Action Client Server

A professional ROS2 Action communication project using a custom `CountUntil.action` interface with Action Client and Action Server architecture.

This project demonstrates:

* ROS2 Actions
* Custom Action Interfaces
* Action Server
* Action Client
* Goal Handling
* Result Processing
* Asynchronous Communication
* Real-time Execution Workflow
* Industry-style ROS2 Package Structure
  
---

# Project Overview

This project implements a complete ROS2 Action workflow.

The Action Client sends a goal to the Action Server.
The Action Server receives the goal and starts counting from 0 up to the target number with a delay between each count.

After execution is complete, the server returns the final result back to the client.

This project is useful for understanding:

* Long-running tasks in ROS2
* Why Actions are better than Services for long tasks
* Client-server communication in robotics
* Asynchronous execution
* Goal/result handling

---

# ROS2 Action Workflow

```text
Action Client  ----------------->  Action Server
      |                                |
      |-------- Send Goal ------------>|
      |                                |
      |<------- Goal Accepted ---------|
      |                                |
      |<-------- Feedback -------------|
      |                                |
      |<--------- Result --------------|
```

---

# Custom Action Interface

File:

```text
action/CountUntil.action
```

Action definition:

```text
# Goal
int64 target_number
float64 delay
---
# Result
int64 reached_number
---
# Feedback
int64 current_number
```

---

# Workspace Structure

```text
action_ws/
│
├── src/
│   ├── my_robot_interface/
│   │   ├── action/
│   │   │   └── CountUntil.action
│   │   ├── CMakeLists.txt
│   │   └── package.xml
│   │
│   └── my_py_pkg/
│       ├── count_until_server.py
│       ├── count_until_client.py
│       ├── package.xml
│       └── setup.py
│
└── install/
```

---

# Features

* Custom ROS2 Action Interface
* Action Server Implementation
* Action Client Implementation
* Goal Acceptance
* Goal Execution
* Result Handling
* Feedback Communication
* Asynchronous Execution
* Professional ROS2 Architecture

---

# Installation

## Clone Repository

```bash
git clone https://github.com/omkar-robotics/ros2-action-client-server.git
```

## Go to Workspace

```bash
cd ros2-action-client-server/action_ws
```

## Build Workspace

```bash
colcon build
```

## Source Workspace

```bash
source install/setup.bash
```

---

# Run the Action Server

Open Terminal 1:

```bash
ros2 run my_py_pkg count_until_server
```

---

# Run the Action Client

Open Terminal 2:

```bash
ros2 run my_py_pkg count_until_client
```

---

# Example Output

## Server Output

```text
[INFO] Action Server Started
[INFO] Received goal request
[INFO] Executing goal...
[INFO] Counting: 1
[INFO] Counting: 2
[INFO] Counting: 3
[INFO] Counting: 4
[INFO] Counting: 5
[INFO] Goal completed
```

## Client Output

```text
[INFO] Goal accepted
[INFO] Current Number: 1
[INFO] Current Number: 2
[INFO] Current Number: 3
[INFO] Current Number: 4
[INFO] Current Number: 5
[INFO] Result: 5
```

---

# Important ROS2 Concepts Used

## Topics

Used for continuous data streaming.

Example:

* Sensor data
* Camera feed
* Robot position

---

## Services

Used for quick request-response communication.

Example:

* Turn LED ON/OFF
* Reset counter

---

## Actions

Used for long-running tasks.

Actions support:

* Goal
* Result
* Feedback
* Cancel Request

Example:

* Robot Navigation
* Autonomous Movement
* Pick and Place Tasks

---

# Why Actions are Important

ROS2 Services are not suitable for long-running tasks because:

No feedback mechanism
No cancellation support
Client waits blindly
Difficult to monitor progress

ROS2 Actions solve these problems using:

Real-time feedback
Goal management
Asynchronous communication
Result handling
Goal cancellation support

This makes Actions ideal for robotics applications.

---

# Technologies Used

* ROS2 Humble
* Python
* rclpy
* colcon
* Ubuntu Linux

---

# Future Improvements

* Goal Cancellation Mechanism
* Multi-Threaded Executor
* Reentrant Callback Groups
* Multiple Goal Handling
* Fibonacci Action Example
* Robot Navigation Actions
* Gazebo Integration
* RViz Visualization
* Real Robot Hardware Integration
---

# Learning Outcome

Through this project, I learned:

* ROS2 Action Architecture
* Custom ROS2 Interfaces
* Client-Server Communication
* Asynchronous Programming in ROS2
* Goal/Result/Feedback Workflow
* ROS2 Package Structure
* Professional Robotics Development Workflow

---

# Author

Omkar Honrao

(Robotics research intern)

GitHub:

[https://github.com/omkar-robotics](https://github.com/omkar-robotics)
