Communicator Subsystem KPIs
============================

This document defines the **Key Performance Indicators (KPIs)** for evaluating the `rescue_communicator` component in the TIAGo Post-Earthquake Rescue Robot system.

Subsystem Overview
-------------------
The Communicator subsystem is responsible for:
- Capturing environmental audio through microphones.
- Relaying communication via speakers.
- Reporting system status updates in real-time.
- Notifying mission progress or critical events.

Audio Capture Rate
-------------------
This measures how many audio samples the system captures every second. We want the sound recording to stay steady and fast for quick reactions. We check it by looking at how often new audio messages are published.

Audio Delivery Success Rate
----------------------------
This shows how many outgoing audio messages are received and played correctly. We want every message to get through without being lost. We measure it by comparing how many messages were sent versus how many were actually used.

Real-Time Reporting Latency
----------------------------
This measures how fast the system reports important events like finding a victim. The quicker it reports, the better for the mission. We check the time between when something happens and when the report is sent.

Notification Accuracy
----------------------
This shows if the mission updates the robot sends are true to what’s actually happening. We want to make sure operators get correct info. We check it by comparing the notifications to real robot states in the system logs.

Audio Quality Consistency
--------------------------
This checks if the audio sounds clear and strong over time. We want the sound to stay easy to hear without weird noise or changes. We measure it by studying how clean and steady the audio signals are.

Summary Table
-------------

.. list-table:: Audio and Reporting KPIs
   :widths: 30 40 30
   :header-rows: 1

   * - KPI
     - Measurement Method
     - Target Value
   * - Audio Capture Rate
     - Topic publish frequency check
     - > 95% uptime
   * - Audio Delivery Success Rate
     - Sent vs played comparison
     - > 98% success
   * - Real-Time Reporting Latency
     - Timestamp difference logging
     - < 0.5 second
   * - Notification Accuracy
     - Cross-check with system logs
     - > 95% accuracy
   * - Audio Quality Consistency
     - Signal analysis (SNR)
     - > 20 dB SNR
