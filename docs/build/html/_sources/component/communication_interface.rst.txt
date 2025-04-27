3. Communication Interface
---------------------------

Manages the interaction between the robot and external operators.

- **Real-time Reporting** (Component: ``Rescue Communicator``):

  - Continuously sends environmental and victim updates.

  - Required: Position from GPS, Medical Report from Triage System, Id ecc from Victim Detection and Reporting, Structural Condition from Risk Assessment
  
  - Provided: Report to Mission Status Notification, Report to Gui Operator

  - **Subscribed Topics**:
    - *(None directly subscribed by Real-Time Reporting component)*

  - **Published Topics**:
    - ``report_update`` (``std_msgs/msg/String``): Real-time status updates sent to Mission Status Notification and GUI Operator.
      - **Content**: JSON with:

        - ``timestamp`` (float): Time when the status was generated.
        - ``status`` (string): Status description (e.g., ``"Audio captured"``, ``"System nominal"``).

- **Mission Status Notification** (Component: ``Rescue Communicator``):
  
  - Aggregates mission data and communicates mission completion.
  
  - Required: Report from Real-time Reporting, commands from GUI Operator
  
  - Provided: Status Code to GUI Operator and Mission Status Notification

  - **Subscribed Topics**:
    - ``report_update`` (``std_msgs/msg/String``): Receives real-time reports to aggregate mission status.

  - **Published Topics**:
    - ``mission_status`` (``std_msgs/msg/String``): Aggregated mission status and updates.
      - **Content**: JSON with:
        
        - ``mission_complete`` (bool): Whether the mission task is completed.
        - ``critical_alerts`` (list of strings): List of critical alerts, if any.
        - ``summary`` (string): General summary of mission status.

- **Graphical User Interface (GUI)** (External interface through ``Rescue Communicator``):
  - Displays mission reports.
  - Allows human operators to issue new commands.
  - Required: Status Code from Mission Status Notification and Report from Real-time Reporting
  - Provided: Command to Mission Status Notification and Autonomous Navigation

  - **Subscribed Topics**:
  
    - ``mission_status`` (``std_msgs/msg/String``): Final mission reports for GUI display.
    - ``report_update`` (``std_msgs/msg/String``): Real-time updates shown live to operators.

  - **Published Topics**:
    - ``gui_commands`` (``std_msgs/msg/String``): Commands from operator to Mission Status Notification or Autonomous Navigation.
      - **Content**: JSON with:
        
        - ``command_type`` (string): Type of command (e.g., ``"Pause"``, ``"Resume"``, ``"New Target"``).
        - ``parameters`` (dict): Command-specific parameters (optional).

- **Microphones** detect audio responses from victims or environmental sounds.
  - Provide: Audio to Victim Detection and Reporting and Triage System
  - **Published Topics**:
    - ``audio_in`` (``std_msgs/msg/String``): Captured audio input.
      - **Content**: Plain text or base64 encoded audio string (depending on system).

- **Speakers** deliver verbal prompts and instructions.
  - Required: Audio from Triage System
  - **Subscribed Topics**:
    - ``search_rescue_audio_out`` (``std_msgs/msg/String``): Audio commands to be spoken.
      - **Content**: Plain text message to be played aloud.

**Interfaces**:

- ``Rescue Core System`` → ``Rescue Communicator``: 

Publishes navigation status updates and system health reports.

- ``Rescue Communicator`` → ``Rescue Core System``: 

Sends operator-issued commands (from GUI) back into the system.

- ``Rescue Communicator`` → ``GUI Operator``: 

Provides real-time reports and mission status updates.

- ``GUI Operator`` → ``Rescue Communicator``: 

Sends commands and instructions for the mission.
