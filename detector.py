# Load libraries
import cv2
import numpy as np
from generate_results import GenerateFinalDetections




frame = cv2.imread('test.jpg')
# Instantiate a new detector
finalDetector = GenerateFinalDetections()

finalDetector.predict(frame)
# load image, convert to RGB, run model and plot detections. 
