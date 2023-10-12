[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oB7VDeFN)
# ExplorationActivity1


1. Which package/library does the sample program demonstrate?

    The sampe program explores the OpenCV(Open Source Computer Vision) and machine learning library in python that is used for image processing and performing computer vision tasks[1]
    It also uses Mediapipe, Google's open-source framework, used for media processing.



2. How does someone run your program?

    The program requires the latest version of opencv and mediapipe to be installed. This was done by using pip commands in the terminal. 

    $ pip install opencv-python
    $ pip install mediapipe

    Once these are installed, the HandTrackModule class can be run on the terminal. The webcam settings might need to be changed depending upon the device [refer to HandTrackModule line 65, line 66]. 

3. What purpose does your program serve?

        The program utilises the Hand Land Mark Model in MediaPipe [picture below] to create a program that tracks the hand movement in real time using the webcam. It also displays frames per second on the live stream, along with the locations of the hands on the terminal. This program can be further developed to detect hands and their movements in live-streams to be used for purposes such as a VR without needing controllers.
<img width="1073" alt="hand-landmarks" src="https://github.com/CS2613-FA23/explorationactivity1-gopikashrivastav/assets/126816880/3d26ae16-9aa3-475d-b591-ef2de3a5e8a4">

   
        
        [2]

        
5. What would be some sample input/output?

    The input is the live webcam feed that tracks hand movements including fingers and wrists, and the output is the location detection.


References:
[1]: https://opencv.org/about/#:~:text=OpenCV%20

[2]: https://developers.google.com/mediapipe/solutions/vision/hand_landmarker
