2. Structural Analysis
----------------------

This subsystem evaluates the surrounding environment for hazards.

- **Obstacle and Damage Detection** (Component: ``Rescue Perception``):
  - Utilises LiDAR, SONAR, and RGB-D sensors.
  - Detects obstacles, cracks, and structural anomalies.
  - Provided: PointCloud to Structural Risk Assessment and Autonomous Navigation
  - Required: PointCloud ecc from Merge Data

  - **Subscribed Topics**:
    - ``/env_detection`` (``std_msgs/msg/String``): Environmental mapping data.
      - **Content**: JSON with:
      
        - ``points_frame_id`` (string): Frame ID reference.
        - ``sonar_range`` (float): SONAR-measured range.
        - ``point_cloud`` (list of [x, y, z] tuples): 3D obstacle points.

  - **Published Topics**:
    - ``/obstacle_position`` (``std_msgs/msg/String``): Detected obstacles or damage areas.
      - **Content**: JSON with:

        - ``timestamp`` (float): Time when detection happened.
        - ``obstacle_detected`` (bool): Whether obstacles were found.
        - ``obstacle_count_estimate`` (int): Estimated number of obstacles.
        - ``infrared_intensity`` (float): Infrared intensity measurement.
        - ``sensor_frame`` (string): Frame ID related to detection.

- **Structural Risk Assessment** (Component: ``Rescue Structural Analysis``):
  - Processes structural data received from ``Rescue Perception``.
  - Evaluates wall stability and floor conditions.
  - Sends risk assessments and safe path suggestions to ``Rescue Core System``.
  - Provided: Command to Autonomous Navigation, Structural Condition to Real-time Reporting

  - **Subscribed Topics**:

    - ``/env_detection`` (``std_msgs/msg/String``): Structural sensing input from Perception.
    - ``/imu_data`` (``std_msgs/msg/String``): IMU measurements to assess physical stress.
      - **Content**:

        - ``linear_acceleration`` (dict with x, y, z): Forces measured.
        - ``angular_velocity`` (dict with x, y, z): Rotational velocities.

  - **Published Topics**:
    - ``/risk_info`` (``std_msgs/msg/String``): Structural collapse risk evaluation.
      - **Content**: JSON with:

        - ``timestamp`` (float): Time of analysis.
        - ``stress_value`` (float): Magnitude of detected stress (normalized).
        - ``angle_variation`` (float): Detected angular shift.
        - ``collapse_risk`` (float): Risk score (0–1).
        - ``risk_level`` (string): ``HIGH`` or ``LOW`` risk classification.

**Interfaces**:

- ``Rescue Perception`` → ``Rescue Structural Analysis``: 

Publishes environment mapping and IMU data (``/env_detection``, ``/imu_data`` topics).

- ``Rescue Structural Analysis`` → ``Rescue Core System``: 

Publishes structural risk evaluations and obstacle alerts (``/risk_info``, ``/obstacle_position`` topics).
