import cv2
import os
import numpy as np
from PIL import Image

def train_classifier():
    data_dir = "photos"
    path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

    faces = []
    ids = []

    for image_path in path:
        filename = os.path.basename(image_path)
        
        # Expect format: user.<id>.<count>.jpg
        parts = filename.split('.')
        if len(parts) < 3 or not parts[1].isdigit():
            print(f"❌ Skipping invalid filename format: {filename}")
            continue

        try:
            img = Image.open(image_path).convert('L')  # grayscale
            image_np = np.array(img, 'uint8')
            id = int(parts[1])
            faces.append(image_np)
            ids.append(id)
        except Exception as e:
            print(f"⚠️ Error processing {filename}: {e}")

    if len(set(ids)) < 2:
        print(f"❌ Not enough unique student IDs. At least 2 different users required.")
        return

    if len(faces) < 2:
        print(f"❌ Not enough training data. At least 2 face images required.")
        return

    ids = np.array(ids)

    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces, ids)
    clf.save("trainer.yml")
    print("✅ Training complete! Model saved to trainer.yml.")

if __name__ == "__main__":
    train_classifier()
