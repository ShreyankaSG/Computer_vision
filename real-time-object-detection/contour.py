import cv2
import numpy as np
import pyrealsense2 as rs
import imutils
pipeline=rs.pipeline()
pipeline.start()

while True:
	frames=pipeline.wait_for_frames()
	depth=frames.get_depth_frame()
	depth_image=np.asanyarray(depth.get_data())
	depth_color=cv2.applyColorMap(cv2.convertScaleAbs(depth_image,alpha=0.05),cv2.COLORMAP_HOT)
	grayFrame=cv2.cvtColor(depth_color,cv2.COLOR_BGR2GRAY)
	color_frame=frames.get_color_frame()
	color_image=np.asanyarray(color_frame.get_data())
	frame=imutils.resize(color_image,width=400)
	frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

	dim = frame.shape
	x = int(dim[1]/2)
	y = int(dim[0]/2)
	print(x,y)
	R = frame[y,x,0]
	G = frame[y,x,1]
	B = frame[y,x,2]
	print(B,G,R)
	image_copy=np.copy(frame)
	lower_black=np.array([0,0,0])
	upper_black=np.array([30,30,30])
	mask=cv2.inRange(image_copy,lower_black,upper_black)
	masked_image=np.copy(image_copy)
	masked_image[mask!=0]= [0,0,0]
	crop_background=np.copy(frame)
	crop_background[mask == 0]=[0,0,0]
	complete_image=masked_image+crop_background
	cv2.imshow("final", mask)
	#cv2.imshow("masked_image",masked_image)
	#cv2.imshow("crop_background",crop_background)
	#cv2.imshow("complete_image",complete_image)
	key=cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break

	