5. Actuator Subsystem
^^^^^^^^^^^^^^^^^^^^^^

This subsystem is responsible for executing movement commands received from the core system by controlling the robot's motors.

- **Motor Control** (Component: ``Rescue Actuator``):
  - Controls left and right motors independently based on incoming commands.
  - Executes movement patterns like forward, backward, turning, and stopping.

  - **Subscribed Topics**:
    - ``motor_commands`` (``std_msgs/msg/String``): Motor actuation commands for movement control.
      - **Content**: JSON with:

        - ``left`` (int or float): Speed value for the left motor (positive for forward, negative for backward).
        - ``right`` (int or float): Speed value for the right motor (positive for forward, negative for backward).

  - **Published Topics**:
    - *(None currently published by Actuator Node)*

- **Internal Modules**:

  - **Motor Controller**: Manages coordinated control of both left and right motors.
  - **Motors**: Low-level execution of movement commands including forward motion, backward motion, and stopping.

**Interfaces**:

- ``Rescue Core System`` → ``Rescue Actuator``: 

Sends motor control commands (via ``motor_commands`` topic).

