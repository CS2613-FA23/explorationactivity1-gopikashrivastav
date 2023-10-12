# Hand Tracker Module


**Questions**

1. Which package/library did you select?

    The sampe program explores the OpenCV(Open Source Computer Vision) and machine learning library along with MediaPipe.


2. What is the package/library?

    OpenCV(Open Source Computer Vision) and machine learning library in python is used for image processing and performing computer vision tasks[1]
    Mediapipe is Google's open-source framework, used for media processing.



• What purpose does it serve?

    The program utilises the Hand Land Mark Model in MediaPipe [picture below] to create a program that tracks the hand movement in real time using the webcam. It also displays frames per second on the live stream, along with the locations of the hands on the terminal. This program can be further developed to detect hands and their movements in live-streams to be used for purposes such as a VR without needing controllers.
<img width="1073" alt="hand-landmarks" src="https://github.com/CS2613-FA23/explorationactivity1-gopikashrivastav/assets/126816880/3d26ae16-9aa3-475d-b591-ef2de3a5e8a4">

• How do you use it?

    The program requires the latest version of opencv and mediapipe to be installed. This was done by using pip commands in the terminal. 

    $ pip install opencv-python
    $ pip install mediapipe

    Once these are installed, the HandTrackModule class can be run on the terminal. The webcam settings might need to be changed depending upon the device [refer to HandTrackModule line 65, line 66]. 

3. What are the functionalities of the package/library?

    OpenCV is a cross-platform library using which we can develop real-time computer vision applications. It mainly focuses on image processing, video capture and analysis including features like face detection and object detection [1]




• Snippets of code and examples of output should be given here.


4. When was it created?


5. Why did you select this package/library?

    This library was chosen as it is extremely relevant with the recent growth in the fields of Artifical Intelligence and Machine Learning. The hand tracking module is a basic module that can be further developed for automation purposes, such as controlling devices using only hand movement detection as well as using it to recognize sign language in real time.

6. How did learning the package/library influence your learning of the language?

    In learning about OpenCV and MediaPipe, I have increased my knoweldge base and understanding of classes and object oriented programming in python.

7. How was your overall experience with the package/library?

    It was a very interesting experience to be able to utilize this library and understand how it can be used to implement a variety of automation projects. 

• When would you recommend this package/library to someone?
    I would recommend OpenCV and MediaPipe to someone that is interested in understanding the basics of artificial intelligence and machine learning, as well as media processing for automation.

• Would you continue using this package/library? Why or why not?

    Yes, I would defintely continue using this library, and specifically look forward to utilize the hand tracking module to build more projects. 


References:

[1]: https://www.tutorialspoint.com/opencv/opencv_overview.htm#:~:text=OpenCV%20is%20a%20cross%2Dplatform,the%20term%20%22Computer%20Vision%22.