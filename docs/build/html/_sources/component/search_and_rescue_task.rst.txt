1. Search and Rescue Task
-------------------------

This subsystem encompasses victim detection, prioritization, and interaction.

- **Victim Detection and Reporting** component: Detects victims through RGB-D and microphone data.

  - **Interfaces**:

    - Required:

      - ``Position`` (type ``Odometry``, Stronglytype) from the ``GPS``;
      - ``Audio`` (Stronglytype) from the ``Microphone``;
      - ``RBD / Point Cloud / Depth / Infrared`` (Stronglytype) from the ``RGB-D Camera``;
    - Provided: ``Stateless`` → ``Autonomus Navigation``;
    - Provide victim localization, ID victims, and priority levels to the ``Triage System`` and ``Autonomus Navigation``.

  - **Subscribed Topics**:
    - ``injury_detection`` (``std_msgs/msg/String``): Injury-related image and RGB-D adjusted data.
      - **Content**: JSON with:

        - ``adjusted_data`` (string): Adjusted image data.
        - ``brightness`` (float): Brightness factor.
        - ``contrast`` (float): Contrast factor.

    - ``audio_in`` (``std_msgs/msg/String``): Captured audio data from the environment.
      - **Content**: Raw audio string, typically voice or environment noise.

  - **Published Topics**:
    - ``search_rescue_audio_out`` (``std_msgs/msg/String``): Consolidated victim detection and triage status.
      - **Content**: JSON with:

        - ``detection`` (dict): Victim detection information.

          - ``timestamp`` (float): Time of detection.
          - ``confidence`` (float): Detection confidence score.
          - ``location`` (dict): Victim location (e.g., lat/lon).
          - ``source`` (string): Detection source (audio/visual).
        - ``triage`` (dict): Victim triage prioritization.
        
          - ``timestamp`` (float): Time of triage.
          - ``priority`` (int): Priority level (1–5).
          - ``reason`` (string): Reason for assigned priority.

- **Triage System** component:

  - Provided: Audio to Speakers, String to RT-Reporting
  - Required: RGB-D ecc from RGB-D Cameras, Status Code from Mission Status Notification
  - Interacts verbally with victims using speakers and microphones.
  - Assesses victim responsiveness through predefined verbal interactions.
  - Sends critical condition alerts to the ``Rescue Core System``.

**Interfaces**:

- ``Rescue Search Tasks`` → ``Rescue Core System``: 

Victim localization, triage results.

- ``Rescue Search Tasks`` → ``Rescue Communicator``: 

Sends detected audio prompts to be played via speakers (``search_rescue_audio_out`` topic).
