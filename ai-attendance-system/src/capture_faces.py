import cv2
import os

# Ask for student name
student_name = input("Enter Student Name: ").strip()

# Create student folder
dataset_path = os.path.join("dataset", student_name)
os.makedirs(dataset_path, exist_ok=True)

# Load Haar Cascade
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Start webcam
camera = cv2.VideoCapture(0)

count = 0
max_images = 50

print("\nCamera Started...")
print("Press 'q' anytime to quit.\n")

while True:

    ret, frame = camera.read()

    if not ret:
        print("Failed to access camera.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:

        face = frame[y:y+h, x:x+w]

        count += 1

        image_path = os.path.join(
            dataset_path,
            f"{count}.jpg"
        )

        cv2.imwrite(image_path, face)

        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"Images: {count}/{max_images}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,255,0),
            2
        )

    cv2.imshow("Dataset Collection", frame)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

    if count >= max_images:
        break

camera.release()
cv2.destroyAllWindows()

print("\nDataset Collection Completed!")