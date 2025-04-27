Search and Rescue Tasks KPIs
=============================

This document defines the **Key Performance Indicators (KPIs)** for evaluating the `rescue_search_tasks` component in the TIAGo Post-Earthquake Rescue Robot system.

Subsystem Overview
-------------------
The Search and Rescue Tasks subsystem is responsible for:
- Detecting potential victims based on sensor and audio data.
- Prioritizing victims based on severity and context.
- Communicating findings to the communication subsystem.


Victim Detection Precision
---------------------------
Precision means how often the system finds real victims without making mistakes. We want it to be really good at only pointing out real victims, not random things. To check it, we compare what it finds to what’s actually there.

Victim Detection Recall
------------------------
Recall is about making sure the system finds every victim, without missing any. We don’t want to leave anyone behind! We check it by seeing how many real victims it finds compared to how many were really there.

Triage Accuracy
---------------
Triage accuracy means how well the system decides how badly someone needs help. It’s important because it helps save the people who need it the most first. We check this by comparing its decisions to what real doctors would choose.

Detection Reaction Time
------------------------
This is how fast the system reacts after it gets new information. In an emergency, every second counts! We measure how much time it takes from getting the data to sending out a warning.

Reporting Success Rate
-----------------------
This is about making sure the system doesn’t just find victims but also successfully tells the people in charge. We want every important message to get through. We check it by seeing if the messages are sent and received correctly.


Summary Table
-------------

.. list-table:: KPI Metrics
   :widths: 30 40 30
   :header-rows: 1

   * - KPI
     - Measurement Method
     - Target Value
   * - Victim Detection Precision
     - Ground truth comparison
     - > 85%
   * - Victim Detection Recall
     - Ground truth comparison
     - > 90%
   * - Triage Accuracy
     - Human expert validation
     - > 85%
   * - Detection Reaction Time
     - Timestamp logging
     - < 1 second
   * - Reporting Success Rate
     - Message transmission tracking
     - > 98%
