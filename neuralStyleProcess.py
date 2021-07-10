import imutils,cv2,os
import numpy as np

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def neuralStyleTransfer(directoryName, filename, selected_style):
	# Neural style transfer codes adapted from pyimageSearch
	# Load Style Model
	target = os.path.join(APP_ROOT, 'static/models/')
	net = cv2.dnn.readNetFromTorch(target + selected_style)

	# load the input image & resize it to have a width of 600 pixels
	image = cv2.imread(directoryName+filename)
	image = imutils.resize(image, width=600)
	(h, w) = image.shape[:2]

	# construct a blob from the image, set the input, and then perform a forward pass of the network
	blob = cv2.dnn.blobFromImage(image, 1.0, (w, h),
		(103.939, 116.779, 123.680), swapRB=False, crop=False)
	net.setInput(blob)
	output = net.forward()

	# reshape the output tensor, add back in the mean subtraction
	output = output.reshape((3, output.shape[2], output.shape[3]))
	output[0] += 103.939
	output[1] += 116.779
	output[2] += 123.680
	# Swap the channel ordering
	output = output.transpose(1, 2, 0)

	filename, file_extension = os.path.splitext(filename)
	generatedFile = 'GeneratedImage'+ '_' + filename + file_extension
	cv2.imwrite(directoryName + generatedFile, output)
	return generatedFile

if __name__=='__main__':
	neuralStyleTransfer('', 'my_content.jpg', 'gold_black_2700.t7')