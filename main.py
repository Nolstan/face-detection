import cv2
import mediapipe as mp


# It is used to detect all the facial landmarks in real-time
mp_drawing = mp.solutions.drawing_utils 

# It is used to estimate the facial landmarks
mp_face_mesh = mp.solutions.face_mesh

drawing_specs = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
# Start capturing video from my default camera
video = cv2.VideoCapture(0) #0 → first camera

with mp_face_mesh.FaceMesh( max_num_faces=2,min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:


    while True:
        # Read a frame from the video capture
        ret, frame = video.read()
        frame = cv2.flip(frame, 1)  # Flip horizontally
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        face_mesh_results = face_mesh.process(image)
        # print(face_mesh_results)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        # Draw the facial landmarks on the frame    
        if face_mesh_results.multi_face_landmarks:
            for face_landmarks in face_mesh_results.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    image=frame,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_TESSELATION, 
                    landmark_drawing_spec=drawing_specs,            
                    connection_drawing_spec=drawing_specs          
                )

       

        cv2.imshow("Face Mesh", frame)

        K = cv2.waitKey(1)

        if K == ord('q'):
            break

    # Release the video capture object and close all OpenCV windows
    video.release()
    cv2.destroyAllWindows