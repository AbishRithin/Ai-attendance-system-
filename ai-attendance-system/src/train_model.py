import os
import pickle
import face_recognition

DATASET_DIR = "dataset"
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "encodings.pkl")

known_encodings = []
known_names = []

os.makedirs(MODEL_DIR, exist_ok=True)

print("Training started...\n")

for person_name in os.listdir(DATASET_DIR):
    person_path = os.path.join(DATASET_DIR, person_name)

    if not os.path.isdir(person_path):
        continue

    print(f"Processing: {person_name}")

    for image_name in os.listdir(person_path):
        image_path = os.path.join(person_path, image_name)

        try:
            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)

            if len(encodings) == 0:
                print(f"  Skipped {image_name} (No face found)")
                continue

            known_encodings.append(encodings[0])
            known_names.append(person_name)

        except Exception as e:
            print(f"  Error in {image_name}: {e}")

data = {
    "encodings": known_encodings,
    "names": known_names
}

with open(MODEL_PATH, "wb") as f:
    pickle.dump(data, f)

print("\nTraining Completed Successfully!")
print(f"Total Faces Learned: {len(known_names)}")
print(f"Model Saved: {MODEL_PATH}")