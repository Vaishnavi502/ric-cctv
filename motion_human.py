import numpy as np
import cv2

net = cv2.dnn.readNet("yolov3-tiny.weights", "yolov3-tiny.cfg")
classes = []
with open("coco.names", "r") as f:
    classes = f.read().strip().split("\n")
# print(classes)
video = cv2.VideoCapture("delivery.mp4")

while True:
    status, frame = video.read()
    if not status:
        break

    height, width, _ = frame.shape
    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    outs = net.forward(net.getUnconnectedOutLayersNames())

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = int(detection[1])
            confidence = scores[class_id]

            if confidence > 0 and class_id == 0:  # Detect person
                box = detection[0:4] * np.array([width, height, width, height])
                (x, y, w, h) = box.astype("int")

                label = classes[class_id]
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Object Detection", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()