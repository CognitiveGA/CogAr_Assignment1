Structural Analysis KPIs
==========================

This document defines the **Key Performance Indicators (KPIs)** for evaluating the `rescue_structural_analysis` component in the TIAGo Post-Earthquake Rescue Robot system.

Subsystem Overview
-------------------
The Structural Analysis subsystem is responsible for:
- Assessing environmental risks (e.g., potential collapse) based on structural sensor data.
- Detecting debris, obstacles, and structural damages.
- Providing actionable data to the core system for navigation and mission planning.

Collapse Risk Assessment Accuracy
----------------------------------
This measures how well the system predicts building risks compared to what experts say. We want it to be very accurate so rescue missions stay safe. We check it by comparing predictions with real or simulated ground truth data.

Obstacle Detection Reliability
-------------------------------
This shows how good the system is at spotting obstacles like debris without missing or inventing anything. We want it to find all real obstacles and avoid mistakes. We test it in places where we already know what’s there.

Structural Analysis Reaction Time
----------------------------------
This is how quickly the system analyzes new data and reports risks or obstacles. Fast reaction is important for quick decisions. We time how long it takes from getting the data to sending out a report.

Processing Success Rate
------------------------
This measures how often the system handles all the incoming data correctly without crashing or getting stuck. We want it to work smoothly even in tough environments. We count how many tasks it finishes successfully.

False Alarm Rate
----------------
This tells us how often the system gives a warning when there’s actually no problem. We want as few false alarms as possible so we don’t waste time. We check it by comparing alerts to what’s truly happening in the environment.

Summary Table
-------------

.. list-table:: Collapse Risk Detection KPIs
   :widths: 30 40 30
   :header-rows: 1

   * - KPI
     - Measurement Method
     - Target Value
   * - Collapse Risk Accuracy
     - Ground truth comparison
     - > 90%
   * - Obstacle Detection Reliability
     - Validation against test scenes
     - > 85%
   * - Reaction Time
     - Timestamp logging
     - < 1 second
   * - Processing Success Rate
     - Message processing tracking
     - > 99%
   * - False Alarm Rate
     - Ground truth validation
     - < 5%
