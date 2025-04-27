4. Core System
--------------

The brain of the robot, managing and coordinating all subsystems.

- **SLAM** (Component: ``Rescue Core System``):

  - Integrates inputs from perception, structural analysis, and search tasks.
  - Decides on movement, inspection, reporting, and interaction priorities.
  - Sends movement goals and actuation commands to ``Rescue Actuator``.
  
  - **Subscribed Topics**:

    - ``env_detection`` (``std_msgs/msg/String``): Environment mapping and obstacle detection data.

      - **Content**: JSON with:

        - ``points_frame_id`` (string): Frame ID from LiDAR.

        - ``sonar_range`` (float): SONAR range measurement.

        - ``point_cloud`` (list of [x, y, z] tuples): 3D points used to generate the map.

  - **Published Topics**:

    - ``navigation_status`` (``std_msgs/msg/String``): Status updates of navigation plans.

      - **Content**: JSON with:
      
        - ``status`` (string): Result status, e.g., ``SUCCESS``, ``ABORTED``.
        - ``estimated_time`` (integer): Estimated time to complete navigation (in seconds).
  
- **Autonomous Navigation Module**: 

  - Plans navigation routes based on generated maps.
  - Required: Information from ``Structural Risk Assessment``, ``Point Cloud`` from ``Obstacels and Damage Detection``, ``Status Code``from ``Mission Status Notification``, ``Commands``from ``GUI Operator``, and ``Localization``, ``ID victims``, and ``Priority`` from ``Victim Detection and Reporting``.
  - Sends the ``Path`` to the ``Motor Controllers``.
  - **Required Inputs**:

    - PointCloud and SONAR data from ``Rescue Perception`` (via ``env_detection`` topic).

  - **Provided Outputs**:
  
    - Navigation status updates (via ``navigation_status`` topic).
    - Navigation decisions and motion plans sent internally to ``Rescue Actuator`` (implementation details abstracted).

- **Interfaces**:

  - ``Rescue Core System`` ← ``Rescue Perception``: 
  
  Subscribes to environment detection data (``env_detection`` topic).

  - ``Rescue Core System`` → ``Rescue Actuator``: 
  
  Sends navigation goals and motion commands (internal interface).

  - ``Rescue Core System`` → ``Rescue Communicator``: 
  
  Sends navigation status updates (via ``navigation_status`` topic).
