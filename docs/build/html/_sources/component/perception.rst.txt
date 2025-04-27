6. Perception Subsystem
-----------------------

Responsible for acquiring and processing raw sensory data.

- **Environmental Perception**:

  - Fuses RGB-D, LiDAR, and SONAR data to generate 3D maps.
  - Detects victims, obstacles, and structural damages.

  - **Subscribed Topics**:

    - ``/scan_raw`` (``sensor_msgs/msg/PointCloud2``): 

    Raw point cloud data from LiDAR for obstacle and structure mapping.

    - ``/sonar_base`` (``sensor_msgs/msg/Range``): 

    Range measurements for detecting nearby obstacles.

    - ``/head_front_camera/rgb/image_raw`` (``sensor_msgs/msg/Image``): 

    RGB images for victim and injury detection.

    - ``/base_imu`` (``sensor_msgs/msg/Imu``): 

    Inertial data (linear acceleration and angular velocity) for stability and motion analysis.
    
    - ``/ground_truth_odom`` (``nav_msgs/msg/Odometry``): 

    Odometry readings serving as GPS position data.

  - **Published Topics**:

    - ``env_detection`` (``std_msgs/msg/String``): Environment mapping and obstacle detection data.
      
      - **Content**: JSON with:

        - ``points_frame_id`` (string): Frame ID from LiDAR.
        - ``sonar_range`` (float): SONAR range measurement.
        - ``point_cloud`` (list of [x, y, z] tuples): Example or detected points.

    - ``injury_detection`` (``std_msgs/msg/String``): Injury detection and adjusted RGB camera data.
      
      - **Content**: JSON with:

        - ``adjusted_data`` (string): Simulated adjusted image data.
        - ``brightness`` (float): Brightness level applied.
        - ``contrast`` (float): Contrast level applied.

    - ``imu_data`` (``std_msgs/msg/String``): Processed IMU readings.
      
      - **Content**: JSON with:

        - ``linear_acceleration`` (dict with x, y, z): Linear acceleration from IMU.
        - ``angular_velocity`` (dict with x, y, z): Angular velocity from IMU.

    - ``gps_position`` (``std_msgs/msg/String``): Robot position extracted from GPS/odometry.
      
      - **Content**: JSON with:

        - ``position`` (dict with x, y, z): Current robot position.

    - **Localization Sensors**:
      - GPS (for outdoor/global localization).
      - IMUs (Inertial Measurement Units) for enhanced accuracy indoors.

- **Interfaces**:

  - ``Perception`` → ``Core System``: 

  Publishes real-time mapping and obstacle information (``env_detection`` topic).

  - ``Perception`` → ``Structural Analysis``: 

  Provides raw structural sensing data (direct data interface).

  - ``Perception`` → ``Search and Rescue Task`
  - ``Perception`` → ``Communicator``