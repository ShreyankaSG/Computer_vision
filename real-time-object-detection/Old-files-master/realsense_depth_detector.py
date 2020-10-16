import pyrealsense2 as rs
import numpy as np
import cv2

pipeline = rs.pipeline()
pipeline.start()

try:
  while True:
    #Create a pipeline object. This object configures the camera and owns its handle
    frames = pipeline.wait_for_frames()
    depth = frames.get_depth_frame()

    if not depth:
        continue

    # Convert images into numpy arrays
    depth_image = np.asanyarray(depth.get_data())


    # Add colorjet to depth map
    depth_color = cv2.applyColorMap(cv2.convertScaleAbs(depth_image,alpha=0.05),cv2.COLORMAP_HOT)
    grayFrame = cv2.cvtColor(depth_color,cv2.COLOR_BGR2GRAY)
    x = (grayFrame[508,718])
    # Distance formula for Intel RealSense
    dist = (0.02591*x) + 0.03047
    dist = round(dist,2)
    print("The Distance of the object from the camera is ",dist," metres!")
    cv2.imwrite('/home/robond/Quadbionics/test2.png',grayFrame)
    cv2.namedWindow('Realsense depth',cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Realsense depth',depth_color)
    cv2.namedWindow('Gray',cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Gray',grayFrame)
    cv2.waitKey(1)

finally:
    #Stop Streaming
    pipeline.stop()
