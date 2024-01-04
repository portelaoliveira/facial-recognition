import pathlib

import cv2

from classes.simple_facerec import SimpleFacerec


def register_user() -> None:
    # Access webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Read webcam frame
        _, frame = cap.read()

        # Show frame on screen
        cv2.imshow("Registro Facial", frame)

        # Check if the 's' key was pressed to save the photo
        if cv2.waitKey(1) & 0xFF == ord("s"):
            # Get username
            nome = input("Digite seu nome: ")

            # Create folder
            folder = pathlib.Path("images/")
            folder.mkdir(parents=True, exist_ok=True)

            # Save photo
            cv2.imwrite(f"images/{nome}.jpg", frame)

            # Exit the loop
            break

    # Turn off webcam
    cap.release()
    cv2.destroyAllWindows()


def facial_rec() -> None:
    # Encode faces from a folder
    sfr = SimpleFacerec()
    sfr.load_encoding_images("images/")

    # Load Camera
    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()

        # Detect Faces
        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

            cv2.putText(
                frame,
                name,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_DUPLEX,
                1,
                (0, 200, 0),
                2,
            )
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 200, 0), 4)

        cv2.imshow("Reconhecimento Facial", frame)

        # Check if the 'q' key was pressed to exit webcam
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Turn off webcam
    cap.release()
    cv2.destroyAllWindows()
