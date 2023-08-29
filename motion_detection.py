# import cv2

# background = cv2.imread("background2.png")
# background = cv2.cvtColor(background,cv2.COLOR_BGR2GRAY)
# background = cv2.GaussianBlur(background,(21,21),0)

# video = cv2.VideoCapture("test3.avi")

# while True:
# 	status, frame = video.read()
# 	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
# 	gray = cv2.GaussianBlur(gray,(21,21), 0)

# 	diff = cv2.absdiff(background,gray)

# 	thresh = cv2.threshold(diff,30,255,cv2.THRESH_BINARY)[1]
# 	thresh = cv2.dilate(thresh, None, iterations = 2)

# 	cnts,res = cv2.findContours(thresh.copy(),
# 		cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 	for contour in cnts:
# 		if cv2.contourArea(contour) < 10000 :
# 			continue
# 		(x,y,w,h) = cv2.boundingRect(contour)
# 		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0), 3)

# 	cv2.imshow("All Contours",frame)

# 	# cv2.imshow("Threshold Video",thresh)

# 	# cv2.imshow("Diff Video",diff)
# 	# cv2.imshow("Gray Video",gray)

# 	key = cv2.waitKey(1)
# 	if key == ord('q'):
# 		break

# video.release()
# cv2.destroyWindows()

# ##################################################################################################
# # Attempt 1.2
# import cv2

# video = cv2.VideoCapture("package_deliv.avi")

# # Background extraction
# background_frames = []
# background_frame_count = 2  # Number of frames for background estimation

# for _ in range(background_frame_count):
#     status, frame = video.read()
#     if not status:
#         break
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     background_frames.append(gray)

# background = cv2.medianBlur(sum(background_frames) // len(background_frames), 21)

# while True:
#     status, frame = video.read()
#     if not status:
#         break

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     gray = cv2.GaussianBlur(gray, (21, 21), 0)

#     diff = cv2.absdiff(background, gray)

#     thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)[1]
#     thresh = cv2.dilate(thresh, None, iterations=2)

#     cnts, res = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     for contour in cnts:
#         if cv2.contourArea(contour) < 10000:
#             continue
#         (x, y, w, h) = cv2.boundingRect(contour)
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

#     cv2.imshow("All Contours", frame)

#     key = cv2.waitKey(1)
#     if key == ord('q'):
#         break

# video.release()
# cv2.destroyAllWindows()


# ####################################################################################################
# # Attempt2
# import cv2

# video = cv2.VideoCapture("amazon_delivery2.avi")

# # Create a background subtractor
# bg_subtractor = cv2.createBackgroundSubtractorKNN()

# while True:
#     status, frame = video.read()
#     if not status:
#         break

#     # Apply background subtraction
#     fg_mask = bg_subtractor.apply(frame)

#     fg_mask = cv2.threshold(fg_mask, 30, 255, cv2.THRESH_BINARY)[1]
#     fg_mask = cv2.dilate(fg_mask, None, iterations=2)

#     # draw rectangles
#     cnts, _ = cv2.findContours(fg_mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     for contour in cnts:
#         if cv2.contourArea(contour) < 10000:
#             continue
#         (x, y, w, h) = cv2.boundingRect(contour)
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

#     cv2.imshow("Motion Detection", frame)

#     key = cv2.waitKey(1)
#     if key == ord('q'):
#         break

# video.release()
# cv2.destroyAllWindows()



# #############################################################################################
# # Attempt3
# import numpy as np
# import cv2


# net = cv2.dnn.readNet("yolov3-tiny.weights", "yolov3-tiny.cfg")
# classes = []
# with open("coco.names", "r") as f:
#     classes = f.read().strip().split("\n")

# video = cv2.VideoCapture("package_deliv.avi")

# while True:
#     status, frame = video.read()
#     if not status:
#         break

#     height, width, _ = frame.shape
#     blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
#     net.setInput(blob)
#     outs = net.forward(net.getUnconnectedOutLayersNames())

#     for out in outs:
#         for detection in out:
#             scores = detection[5:]
#             class_id = int(detection[1])
#             confidence = scores[class_id]

#             if confidence > 0.5:  # Change the confidence threshold as needed
#                 box = detection[0:4] * np.array([width, height, width, height])
#                 (x, y, w, h) = box.astype("int")

#                 cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#                 cv2.putText(frame, classes[class_id], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#     cv2.imshow("Object Detection", frame)

#     key = cv2.waitKey(1)
#     if key == ord('q'):
#         break

# video.release()
# cv2.destroyAllWindows()