Core System KPIs
=================

This document defines the **Key Performance Indicators (KPIs)** for evaluating the `rescue_core_system` component in the TIAGo Post-Earthquake Rescue Robot system.

Subsystem Overview
-------------------
The Core System subsystem is responsible for:
- Building a map of the environment from perception data.
- Planning and executing autonomous navigation to reach goals safely.
- Enabling mission-level decision making based on environmental understanding.

Map Completeness
----------------
This measures how much of the environment the system is able to map while exploring. We want it to cover as much as possible so there are no hidden areas. We check it by comparing the finished map to what the environment really looks like.

Map Quality Score
------------------
This shows how good the map is by checking how accurate and clear it is, even with sensor noise. A good map helps the robot move safely. We measure it using a score from 0 (bad) to 1 (perfect).

Navigation Success Rate
------------------------
This tells us how often the robot finishes its missions without giving up or getting stuck. We want it to complete as many tasks as possible. We check the success or failure reports after each navigation task.

Time to Goal
------------
This measures how long it takes for the robot to reach its target after planning a path. Faster is better, but it still needs to stay safe. We check it by comparing the expected time to how long it actually takes.

Replanning Frequency
---------------------
This shows how often the robot has to change its path because of obstacles or updates to the map. We want to keep this low unless really needed. We track how many times it replans during a mission.

Summary Table
-------------

.. list-table:: Mapping and Navigation KPIs
   :widths: 30 40 30
   :header-rows: 1

   * - KPI
     - Measurement Method
     - Target Value
   * - Map Completeness
     - Coverage comparison
     - > 90%
   * - Map Quality Score
     - Internal scoring
     - > 0.8
   * - Navigation Success Rate
     - Mission tracking
     - > 95%
   * - Time to Goal
     - ETA vs actual time
     - < 10% deviation
   * - Replanning Frequency
     - Event counter
     - < 2 per mission
