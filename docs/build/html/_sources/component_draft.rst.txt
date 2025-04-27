Component Diagram
==================

Graphical Representation
-------------------------

.. note::

   Visual component diagram summarizing the subsystems and their interactions.

.. image:: images/component_diagram.svg
   :alt: Component Diagram
   :align: center

Cognitive Architecture for Robotics – Assignment 1 (2024/25)
-------------------------------------------------------------

**Topic**: Post-Earthquake Scenarios for Search and Rescue

This project designs a cognitive architecture to manage a TIAGo robotic platform operating in post-earthquake environments. The robot is tasked with locating injured individuals, evaluating their medical conditions, and assessing the structural integrity of the environment.

The robot is equipped with the following sensors and devices:

- RGB-D Camera
- LiDAR
- SONAR
- Force Sensors
- Microphones
- Speakers

Primary tasks include:

- **Victim Condition Assessment**: Evaluate consciousness, responsiveness, and injury severity.
- **Structural Hazard Detection**: Identify cracks, unstable sections, and other building risks.
- **Critical Report Transmission**: Send detailed updates about victims and structures to a remote human supervisor.
- **Mission Status Notification**: Notify completion of area exploration and await further instructions.

System Architecture
--------------------

The architecture is divided into interconnected subsystems:

1. Search and Rescue Task
^^^^^^^^^^^^^^^^^^^^^^^^^

This subsystem encompasses victim detection, prioritization, and interaction.

- **Victim Detection and Reporting** component: Detects victims through RGB-D and microphone data.

  - **Interfaces**:

    - Required:

      - ``Position`` (type ``Odometry``, Stronglytype) from the ``GPS``;
      - ``Audio`` (Stronglytype) from the ``Microphone``;
      - ``RBD / Point Cloud / Depth / Infrared`` (Stronglytype) from the ``RGB-D Camera``;

    - Provided: ``Stateless`` → ``Autonomus Navigation``;
    - Provide victim localization, ID victims, and priority levels to the ``Triage System`` and ``Autonomus Navigation``;
    
    .. TODO: write the type of msg 

- **Triage System** component:

  - Provided: Audio to Speakers, String to RT-Reporting
  - Required: RGB-D ecc from RGB-D Cameras, Status Code from Mission Status Notification
  - Interacts verbally with victims using speakers and microphones.
  - Assesses victim responsiveness through predefined verbal interactions.
  - Sends critical condition alerts to the ``Rescue Core System``.
  
  .. TODO: write the type of msg 


**Interfaces**:
- ``Rescue Search Tasks`` → ``Rescue Core System``: Victim localization, triage results.

2. Structural Analysis
^^^^^^^^^^^^^^^^^^^^^^

This subsystem evaluates the surrounding environment for hazards.

- **Obstacle and Damage Detection** (Component: ``Rescue Perception``):

  - Utilises LiDAR, SONAR, and RGB-D sensors.
  - Detects obstacles, cracks, and structural anomalies.
  - Provided: PointCloud to Structural Risk Assessment and Autonomus Navigation
  - Required: PointCloud ecc from Merge Data
  
  .. TODO: write the type of msg 

- **Structural Risk Assessment** (Component: ``Rescue Structural Analysis``):

  - Processes structural data received from ``Rescue Perception``.
  - Evaluates wall stability and floor conditions.
  - Sends risk assessments and safe path suggestions to ``Rescue Core System``.
  - Provided: Command to Autonomous Navigation, Structural Condition to Real-time Reporting

**Interfaces**:
- ``Rescue Perception`` → ``Rescue Structural Analysis``: Structural and obstacle data.
- ``Rescue Structural Analysis`` → ``Rescue Core System``: Risk evaluations and warnings.
 
.. TODO: write the type of msg 

3. Communication Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^

Manages the interaction between the robot and external operators.

- **Real-time Reporting** (Component: ``Rescue Communicator``):

  - Continuously sends environmental and victim updates.
  - Required: Position from GPS, Medical Report from Triage System, Id ecc from Victim Detection and Reporting, Structural Condition from Risk Assessment
  - Provided: Report to Mission Status Notification, Report to Gui Operator
  
  .. TODO: write the type of msg 

- **Mission Status Notification** (Component: ``Rescue Communicator``):

  - Aggregates mission data and communicates mission completion.
  - Required: Report from Real-time Reporting, commands from GUI Operator
  - Provided: Status Code to GUI Operator and Mission Status Notification
  
  .. TODO: write the type of msg 

- **Graphical User Interface (GUI)** (External interface through ``Rescue Communicator``):

  - Displays mission reports.
  - Allows human operators to issue new commands.
  - Required: Status Code from Mission Status Notification and Report from Real-time Reporting
  - Provided: Command to Mission Status Notification and Autonomous Navigation
  
  .. TODO: write the type of msg 

- **Microphones** detect audio responses from victims or environmental sounds.

  - Provide: Audio to Victim Detection and Reporting and Triage System

- **Speakers** deliver verbal prompts and instructions.

  - Required: Audio from Triage System
  
  .. TODO: write the type of msg 

**Interfaces**:
-  → : Status reports and mission data.
-  → : External operator commands.

.. TODO: write the type of msg 

4. Core System
^^^^^^^^^^^^^^

The brain of the robot, managing and coordinating all subsystems.

- **SLAM** (Component: ``Rescue Core System``):

  - Integrates inputs from perception, structural analysis, and search tasks.
  - Decides on movement, inspection, reporting, and interaction priorities.
  - Sends movement goals and actuation commands to ``Rescue Actuator``.
  - Required: PointCloud ecc from Merge Data, Odometry from Motor Encoders
  - Provided: PointCloud to Autonomous Navigation

.. TODO: write the type of msg 

6. Perception Subsystem
^^^^^^^^^^^^^^^^^^^^^^^^

Responsible for acquiring and processing raw sensory data.

- **Environmental Perception** (Component: ``Rescue Perception``):

  - Fuses RGB-D, LiDAR, and SONAR data to generate 3D maps.
  - Detects victims, obstacles, and structural damages.

.. TODO: write the type of msg 

- **Localization Sensors**:

  - GPS (for outdoor/global localization).
  - IMUs (Inertial Measurement Units) for enhanced accuracy indoors.
 
.. TODO: write the type of msg 

**Interfaces**:
- ``Rescue Perception`` → ``Rescue Core System``: Real-time mapping and obstacle information.
- ``Rescue Perception`` → ``Rescue Structural Analysis``: Raw structural sensing data.

.. TODO: write the type of msg 

Subsystem Interaction Summary
------------------------------

- ``Tasks`` suggests search plans and reports victim findings to .
-  assesses risks and advises .
-  coordinates actions, sending motion plans to  and mission updates to .
-  executes physical movements and reports outcomes.
-  ensures continuous operator interaction and updates.

.. TODO

