import cv2
import numpy as np 
import argparse
import time
import os
import sys


WEIGHTS_LOC = 'src/trained_weight/rm_koala/yolov4-tiny_armour.weights'
WEIGHTS_POSE = 'src/trained_weight/rm_koala/yolov4-tiny_pose.weights'
CFG_LOC = 'src/cfg/yolov4-tiny_2class_mod.cfg'
CFG_POSE = 'src/cfg/yolov4-tiny_3class.cfg'
NAMES_LOC = 'src/cfg/rm_armour.names'
NAMES_POSE = 'src/cfg/rm_pose.names'


# load yolo weights and cfg 
def load_yolo(weights, cfg, names):
	net = cv2.dnn.readNet(weights, cfg)
	classes = []
	with open(names, "r") as f:
		classes = [line.strip() for line in f.readlines()]
	layers_names = net.getLayerNames()
	output_layers = [layers_names[i[0]-1] for i in net.getUnconnectedOutLayers()]
	colors = np.random.uniform(0, 255, size=(len(classes), 3))
	return (net, classes, colors, output_layers)

# resizes image
def load_image(img_path):
	# image loading
	img = cv2.imread(img_path)

	# resizing makes it faster?
	# img = cv2.resize(img, None, fx=0.4, fy=0.4)
	height, width, channels = img.shape
	return img, height, width, channels

# accepts image and outputs layers as parameters
def detect_objects(img, net, outputLayers):			
	blob = cv2.dnn.blobFromImage(img, scalefactor=0.00392, size=(320, 320), mean=(0, 0, 0), swapRB=True, crop=False)
	# blob = cv2.dnn.blobFromImage(img, mean=(0, 0, 0), swapRB=True, crop=False)
	net.setInput(blob)
	outputs = net.forward(outputLayers)
	return blob, outputs

# dimensions of boxes
def get_box_dimensions(outputs, height, width):
	boxes = []
	confs = []
	class_ids = []
	for output in outputs:
		for detect in output:
			scores = detect[5:]
			print(scores)
			class_id = np.argmax(scores)
			conf = scores[class_id]
			if conf > 0.3:
				center_x = int(detect[0] * width)
				center_y = int(detect[1] * height)
				w = int(detect[2] * width)
				h = int(detect[3] * height)
				x = int(center_x - w/2)
				y = int(center_y - h / 2)
				boxes.append([x, y, w, h])
				confs.append(float(conf))
				class_ids.append(class_id)

	# max_id = np.argmax(confs)
	# print(confs)
	# print(max_id)
	# print(confs[max_id])
	# conf = [confs[max_id]]
	# box = [boxes[max_id]]
	# print(box)
	# best_class = [class_ids[max_id]]
	
	return boxes, confs, class_ids
	# return conf, box, best_class

def draw_labels(boxes, confs, colors, class_ids, classes, img): 
	indexes = cv2.dnn.NMSBoxes(boxes, confs, 0.5, 0.4)
	font = cv2.FONT_HERSHEY_PLAIN


	for i in range(len(boxes)):
		if i in indexes:
			x, y, w, h = boxes[i]
			label = str(classes[class_ids[i]])
			color = colors[i]
			cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
			cv2.putText(img, label, (x, y - 5), font, 1, color, 1)
	cv2.imshow("Image", img)

def image_detect(img_path): 
	# model, classes, colors, output_layers = load_yolo()
	image, height, width, channels = load_image(img_path)
	blob, outputs = detect_objects(image, model, output_layers)
	boxes, confs, class_ids = get_box_dimensions(outputs, height, width)
	# draw_labels(boxes, confs, colors, class_ids, classes, image)
	# while True:
	# 	key = cv2.waitKey(1)
	# 	if key == 27:
	# 		break

def image_detect_loc(img_path, yolo): 
	# model, classes, colors, output_layers = load_yolo()
	model, classes, colors, output_layers = yolo[0], yolo[1], yolo[2], yolo[3]
	image, height, width, channels = load_image(img_path)
	blob, outputs = detect_objects(image, model, output_layers)
	boxes, confs, class_ids = get_box_dimensions(outputs, height, width)
	draw_labels(boxes, confs, colors, class_ids, classes, image)
	print(boxes, confs, class_ids)
	print(len(confs))
	while True:
		key = cv2.waitKey(1)
		if key == 27:
			break

def webcam_detect():
	model, classes, colors, output_layers = load_yolo()
	cap = start_webcam()
	while True:
		_, frame = cap.read()
		height, width, channels = frame.shape
		blob, outputs = detect_objects(frame, model, output_layers)
		boxes, confs, class_ids = get_box_dimensions(outputs, height, width)
		draw_labels(boxes, confs, colors, class_ids, classes, frame)
		key = cv2.waitKey(1)
		print(key)
		if key == 27:
			break
	cap.release()


def start_video(video_path):
	model, classes, colors, output_layers = load_yolo()
	cap = cv2.VideoCapture(video_path)
	while True:
		_, frame = cap.read()
		height, width, channels = frame.shape
		blob, outputs = detect_objects(frame, model, output_layers)
		boxes, confs, class_ids = get_box_dimensions(outputs, height, width)
		draw_labels(boxes, confs, colors, class_ids, classes, frame)
		key = cv2.waitKey(1)
		if key == 27:
			break
	cap.release()


# image_detect(os.path.abspath('images/' + sys.argv[1]))
yolo_loc = load_yolo(WEIGHTS_LOC, CFG_LOC, NAMES_LOC)
yolo_pose = load_yolo(WEIGHTS_POSE, CFG_POSE, NAMES_POSE)
image_detect_loc(os.path.abspath('src/images/200-249/red1 200-249 armour/obj_train_data/red_1_frame0202.jpg'), yolo_pose)

# to do:
# draw labels: get one box
# separate class to draw