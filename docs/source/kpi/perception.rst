Perception Subsystem KPIs
==========================

This document defines the **Key Performance Indicators (KPIs)** for evaluating the `rescue_perception` component in the TIAGo Post-Earthquake Rescue Robot system.

Subsystem Overview
-------------------
The Perception subsystem is responsible for:
- Acquiring environmental and situational data through various sensors (camera, LiDAR, SONAR, GPS, IMU).
- Processing sensor data to produce reliable environmental measurements.
- Providing high-quality data streams to downstream subsystems (search & rescue tasks, structural analysis, core system).

Sensor Data Availability
-------------------------
This checks how often the system successfully gets and shares sensor information over time. We want the sensors to work all the time without dropping data. We measure it by comparing how much data we expected to how much we actually got.

Sensor Data Accuracy
---------------------
This shows how correct the sensor readings are compared to the real world. We want the sensors to be as close to perfect as possible. We check it by comparing sensor results to what we know is true.

Sensor Fusion Latency
----------------------
This measures how fast the system combines different sensor inputs into useful information. The faster, the better for real-time actions. We check it by timing how long it takes from getting raw data to sharing the results.

Environmental Representation Completeness
------------------------------------------
This is about how well the system captures the full shape of the environment, like 3D maps or heat images. We want it to cover everything without missing spots. We measure it by checking the detail and gaps in the data.

IMU/GPS Stability
------------------
This checks how steady the location and movement data stays over time when not moving. Good stability means no drifting or random jumps. We measure it by looking at how much the readings change when they should stay still.

Summary Table
-------------

.. list-table:: Sensor Data KPIs
   :widths: 35 40 25
   :header-rows: 1

   * - KPI
     - Measurement Method
     - Target Value
   * - Sensor Data Availability
     - Message rate monitoring
     - > 98% uptime
   * - Sensor Data Accuracy
     - Ground truth comparison
     - < 5% error
   * - Sensor Fusion Latency
     - Timestamp difference logging
     - < 0.5 second
   * - Environmental Representation Completeness
     - Density and continuity analysis
     - > 90% area
   * - IMU/GPS Stability
     - Variance analysis
     - < 2% drift
