# Crosswalk-Traffic-Analyzer

This project uses the [Tensorflow Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection)
 to monitor vehicle and pedestrian traffic in a roadway. 
 
Using a webcam, this tool will count the number of pedestrians and vehicles that are within the frame of the camera at a given time. The number of pedestrians and vehicles will then be stored in a csv file titled `traffic_results.csv` along with a timestamp of when the counts occured. The tool runs in realtime, the number of frames per second depend on your computer hardware. 
 
The research paper behind this system is found in the repo.

## Installation

* Follow the installation instructions found [here](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md) to install Tensorflow Object Detection

* The tool also depends on OpenCV 3 the install link can be found [here](https://docs.opencv.org/3.4.6/df/d65/tutorial_table_of_content_introduction.html)

## Usage

* In the cloned repository, run `python ./my_detector/traffic_analyzer.py`
* Optional arguments
  * Device index of the camera `--source=0`
  * Width of the video frame `--width=480`
  * Height of the frames in the video stream `--height=360`
  * Number of workers `--num-workers=2`
  * Size of the queue `--queue-size=5`
  * Get video from HLS stream rather than webcam '--stream-input=http://somertmpserver.com/hls/live.m3u8'
  * Send stream to livestreaming server '--stream-output=--stream=http://somertmpserver.com/hls/live.m3u8'
