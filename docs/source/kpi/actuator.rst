Actuator Subsystem KPIs
========================

This document defines the **Key Performance Indicators (KPIs)** for evaluating the `rescue_actuator` component in the TIAGo Post-Earthquake Rescue Robot system.

Subsystem Overview
-------------------
The Actuator subsystem is responsible for:
- Executing movement commands via left and right motors.
- Ensuring consistent, coordinated motor actions.
- Maintaining stable, accurate movement under varying loads.

Command Execution Latency
--------------------------
This measures how fast the motor starts moving after getting a movement command. We want the motors to react as quickly as possible. We check it by recording the time between when the command is received and when the motor starts.

Motion Error
------------
This shows how close the motor's actual movement is to what was asked for. We want it to move exactly as planned without drifting or going too slow. We measure it by comparing the requested movement to what really happened.

Synchronization Accuracy
--------------------------
This checks if the left and right motors move together properly during turns or straight driving. We want them perfectly synced so the robot doesn’t drift. We measure it by looking at the difference between their speeds or travel distances.

Motor Reliability
------------------
This shows how often the motors successfully do what they’re told without problems. We want the motors to work smoothly most of the time. We measure it by counting how many motor actions work versus how many fail.

Safe Stop Capability
---------------------
This checks if the motors can stop safely when they’re told to, like when there's an obstacle. A quick and safe stop is really important. We measure it by checking how long and how far the robot moves after a stop command.

Summary Table
-------------

.. list-table:: Mobility and Control KPIs
   :widths: 30 40 30
   :header-rows: 1

   * - KPI
     - Measurement Method
     - Target Value
   * - Command Execution Latency
     - Timestamp difference
     - < 100 ms
   * - Motion Error
     - Speed/displacement comparison
     - < 5% deviation
   * - Synchronization Accuracy
     - Speed difference check
     - < 5% mismatch
   * - Motor Reliability
     - Action success tracking
     - > 99%
   * - Safe Stop Capability
     - Emergency stopping measurement
     - < 0.5 m
