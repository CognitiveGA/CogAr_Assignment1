.. _integration_tests:

Integration Test Documentation
===============================

This document describes the integration tests designed for the rescue robot system. 
Each test ensures that communication and functionality between system modules follow the cognitive architecture layers (Perception, Cognition, Actuation, Communication).

Test Cases Overview
--------------------

**IT-01: Perception to Core System**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- **Purpose**: Validate that `rescue_perception` publishes environment detection messages correctly, and `rescue_core_system` builds a map and plans navigation.
- **Topics**:
  - `env_detection`
- **Test Files**:
  - `rescue_core_system/test/test_perception_to_core.py` (:doc:`Test Description <test_perception_to_core>`)
  - `rescue_core_system/launch/test_perception_core_launch.py`

**IT-02: Communicator to Search Tasks**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- **Purpose**: Ensure that audio captured by `rescue_communicator` is received and processed by `rescue_search_tasks` for victim detection and triage.
- **Topics**:
  - `audio_in`
- **Test Files**:
  - `rescue_search_tasks/test/test_audio_to_detection.py` (:doc:`Test Description <test_audio_to_detection>`)
  - `rescue_search_tasks/launch/test_comm_to_tasks_launch.py`

**IT-03: Search Tasks to Communicator**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- **Purpose**: Validate that victim detection/triage results in `search_rescue_audio_out` being published and spoken by `rescue_communicator`.
- **Topics**:
  - `search_rescue_audio_out`
- **Test Files**:
  - `rescue_communicator/test/test_audio_feedback.py` (:doc:`Test Description <test_audio_feedback>`)
  - `rescue_communicator/launch/test_triage_to_audioout_launch.py`

**IT-04: Perception to Search Tasks**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- **Purpose**: Check that injury data from `rescue_perception` triggers detection and triage in `rescue_search_tasks`.
- **Topics**:
  - `injury_detection`
- **Test Files**:
  - `rescue_search_tasks/test/test_perception_to_triage.py` (:doc:`Test Description <test_perception_to_triage>`)
  - `rescue_search_tasks/launch/test_perception_to_triage_launch.py`

**IT-05: Core System to Actuator**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- **Purpose**: Verify that navigation commands from `rescue_core_system` are received and executed by `rescue_actuator`.
- **Topics**:
  - `motor_commands`
- **Test Files**:
  - `rescue_actuator/test/test_motor_command_reception.py` (:doc:`Test Description <test_motor_command_reception>`)
  - `rescue_actuator/launch/test_core_to_actuator_launch.py`

**IT-06: Full System Chain**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- **Purpose**: Perform a complete end-to-end validation of the full rescue system pipeline from audio capture to motor actuation.
- **Topics**:
  - `audio_in`, `injury_detection`, `env_detection`, `search_rescue_audio_out`, `motor_commands`
- **Test Files**:
  - `rescue_core_system/test/test_full_system_chain.py` (:doc:`Test Description <test_full_system_chain>`)
  - `rescue_core_system/launch/test_full_system_launch.py`

Execution Instructions
========================

This document explains how to prepare, launch, and test the rescue robot system integration tests step-by-step.

Terminal 1: Setup and Build
---------------------------

.. code-block:: bash

   cd cogar_ros2_ws

   # Make sure all git submodules are up to date
   git submodule update --init --recursive

   # Build the workspace
   colcon build

   # Run robot-specific setup script (example: TIAGo setup)
   ./tiago2.sh

Terminal 2: Launch the Required Nodes
-------------------------------------

.. code-block:: bash

   # Source the workspace
   source install/setup.bash

   # Launch files for each integration test:

   # IT-01: Perception to Core System
   ros2 launch rescue_core_system test_perception_core_launch.py

   # IT-02: Communicator to Search Tasks
   ros2 launch rescue_search_tasks test_comm_to_tasks_launch.py

   # IT-03: Search Tasks to Communicator
   ros2 launch rescue_communicator test_triage_to_audioout_launch.py

   # IT-04: Perception to Search Tasks
   ros2 launch rescue_search_tasks test_perception_to_triage_launch.py

   # IT-05: Core System to Actuator
   ros2 launch rescue_actuator test_core_to_actuator_launch.py

   # IT-06: Full System Chain
   ros2 launch rescue_core_system test_full_system_launch.py

Terminal 3: Run the Test and View Results
-----------------------------------------

.. code-block:: bash

   # Source the workspace
   source install/setup.bash

   # Run the individual package tests:

   # IT-01
   colcon test --packages-select rescue_core_system

   # IT-02
   colcon test --packages-select rescue_search_tasks

   # IT-03
   colcon test --packages-select rescue_communicator

   # IT-04
   colcon test --packages-select rescue_search_tasks

   # IT-05
   colcon test --packages-select rescue_actuator

   # IT-06
   colcon test --packages-select rescue_core_system

   # After running the tests, view the results:
   colcon test-result --verbose

Notes
-----

- Always remember to source the workspace (`source install/setup.bash`) in every terminal.
- Launch the correct nodes for the specific test before running the corresponding `colcon test`.
- For the full system test (IT-06), make sure the full system launch file is running before testing.
