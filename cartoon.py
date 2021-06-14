# importing libraries
import tkinter as tk
from tkinter import filedialog as fd
import cv2

def main():
	
	# reading image
	pic = fd.askopenfilename()
	img = cv2.imread(pic)

	#converting image
	color = cv2.bilateralFilter(img, 9, 250, 250)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
	cartoon = cv2.bitwise_and(color, color, mask=edges)
	
	#saving the image
	output = "/home/user/Pictures/cartoon.jpg"
	cv2.imwrite(output, cartoon)
	
if __name__ == "__main__":
	main()