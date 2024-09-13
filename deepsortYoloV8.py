import cv2
from ultralytics import YOLO  
import random;
from tracker import Tracker;
model = YOLO("..\\xbot\\Braindance\\bestV8.pt")  # Open the model

colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for j in range(10)]
tracker = Tracker();
detection_threshold = 0.5
cap = None
def loop():
    while True:
        cap = cv2.VideoCapture("..\\xbot\\Braindance\\vid1.mp4")  # path to your video
        
        while cap.isOpened():
            # Read a frame from the video
            print("Reading")
            success, frame = cap.read()

            fps = cap.get(cv2.CAP_PROP_FPS)

            if success:
                results = model.predict(
                    frame, show_boxes=True, conf=0.8, show=False
                )  # images is a list of PIL images
                for result in results:
                    detections = []
                    for r in result.boxes.data.tolist():
                        x1, y1, x2, y2, score, class_id = r
                        x1 = int(x1)
                        x2 = int(x2)
                        y1 = int(y1)
                        y2 = int(y2)
                        class_id = int(class_id)
                        if score > detection_threshold:
                            detections.append([x1, y1, x2, y2, score])

                    tracker.update(frame, detections)

                    for track in tracker.tracks:
                        bbox = track.bbox
                        x1, y1, x2, y2 = bbox
                        track_id = track.track_id

                        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (colors[track_id % len(colors)]), 3)
                        
                cv2.imshow("Frame",frame)
                # Display the annotated frame
            else:
                # Break the loop if the end of the video is reached
                break  # Release the video capture object and close the display window
            
            
            if cv2.waitKey(1) & 0xFF == ord("q"):
                return

loop() 
if cap:
    cap.release()
cv2.destroyAllWindows()
