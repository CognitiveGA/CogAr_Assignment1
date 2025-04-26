Component Diagram
==================

.. uml::

   @startuml
   title Post-Earthquake Search and Rescue Robot - Component Diagram

   package "TIAGo Post-earthquake Rescueter" as receiver {

     package "Perception" {
       [RGB-D Cameras] --> [Merge data]
       [LiDARs] --> [Merge data]
       [SONARs] --> [Merge data]
       [Merge data] --> [depth / infrared / point cloud]
       [RGB-D Cameras] --> [RGB / depth / infrared / point cloud]
       [IMUs] --> [linear acceleration / angular velocity]
       [GPS] --> [position]
     }

     package "Communicator" {
       [Microphones] --> [audio]
       [audio] --> [Speakers]
       [position] --> [Real-Time Reporting]
       [string - risk eval] --> [Real-Time Reporting]
       [string - triage info] --> [Real-Time Reporting]
       [string - vict info] --> [Real-Time Reporting]
       [Real-Time Reporting] --> [Mission Status Notification]
       [Real-Time Reporting] --> [GUI Operator]
       [Mission Status Notification] --> [GUI Operator]
       [GUI Operator] --> [Mission Status Notification]
       [Microphones] --> [audio]
       [Mission Status Notification] --> [status code]
       [GUI Operator] --> [command]
     }

     package "Search and Rescue Tasks" {
       [audio] --> [Victim Detection and Reporting]
       [RGB / depth / infrared / point cloud] --> [Victim Detection and Reporting]
       [position] --> [Victim Detection and Reporting]
       [status code] --> [Triage System]
       [Victim Detection and Reporting] --> [Triage System]
       [Triage System] --> [audio]
       [Victim Detection and Reporting] --> [vict info]
       [Triage System] --> [triage info]
     }

     package "Structural Analysis" {
       [depth / infrared / point cloud] --> [Structural Risk Assessment]
       [depth / infrared / point cloud] --> [Obstacle and Damage Detection]
       [linear acceleration / angular velocity] --> [Structural Risk Assessment]
       [Obstacle and Damage Detection] --> [Structural Risk Assessment]
       [Obstacle and Damage Detection] --> [point cloud]
       [Structural Risk Assessment] --> [risk info]
       [Structural Risk Assessment] --> [risk eval]
     }

     package "Core System" {
       [depth / infrared / point cloud] --> [SLAM]
       [point cloud] --> [Autonomous Navigation]
       [risk info] --> [Autonomous Navigation]
       [vict info] --> [Autonomous Navigation]
       [status code] --> [Autonomous Navigation]
       [command] --> [Autonomous Navigation]
       [odometry data] --> [SLAM]
       [SLAM] --> [Autonomous Navigation]
       [Autonomous Navigation] --> [path]
     }

     package "Actuator" {
       [path] --> [Motor controllers]
       [Motor controllers] --> [Motors]
       [Motor encoders] --> [Motor controllers]
       [Motor encoders] --> [odometry data]
     }

     ' connections between subsystems
     [audio] --> [audio]
     [status code] --> [status code]
     [command] --> [command]
     [emit audio] --> [Speakers]
     [vict info] --> [Autonomous Navigation]
     [triage info] --> [GUI Operator]
     [vict info] --> [GUI Operator]
     [RGB / depth / infrared / point cloud] --> [Victim Detection and Reporting]
     [depth / infrared / point cloud] --> [Structural Risk Assessment]
     [linear acceleration / angular velocity] --> [Structural Risk Assessment]
     [depth / infrared / point cloud] --> [SLAM]
     [position] --> [Victim Detection and Reporting]
     [status code] --> [Triage System]
     [point cloud] --> [Autonomous Navigation]
     [risk info] --> [Autonomous Navigation]
     [risk eval] --> [GUI Operator]
     [path] --> [Motor controllers]
     [odometry data] --> [SLAM]

   }
   @enduml