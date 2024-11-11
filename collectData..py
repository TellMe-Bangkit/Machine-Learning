# from ultralytics import YOLO
# from ultralytics.yolo.v8.detect.predict import DetectionPredictor
# import cv2

# # Load YOLO model
# model = YOLO("best.pt")  # Pastikan file model 'best.pt' berada di path yang benar

# # Initialize webcam
# cap = cv2.VideoCapture(0)  # Gunakan 0 untuk kamera default

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         print("Tidak ada frame yang terdeteksi. Keluar...")
#         break

#     # Perform detection
#     results = model(frame)

#     # Draw detections on the frame
#     for result in results:
#         boxes = result.boxes
#         for box in boxes:
#             # Get bounding box coordinates
#             x1, y1, x2, y2 = map(int, box.xyxy[0])  # Koordinat kotak pembatas
#             conf = box.conf[0]  # Nilai kepercayaan (confidence score)
#             cls = int(box.cls[0])  # Label kelas

#             # Assuming the labels are a, b, c, d, e
#             label_names = ['a', 'b', 'c', 'd', 'e']
#             label = f"{label_names[cls]} {conf:.2f}"

#             # Draw bounding box and label on the frame
#             cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
#             cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#     # Display the frame with detections
#     cv2.imshow('YOLOv8 Object Detection', frame)

#     # Break on 'q' key press
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release resources
# cap.release()
# cv2.destroyAllWindows()
import cv2
import os
import uuid
def create_folder(folder_path):
    """Membuat folder jika belum ada."""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' telah dibuat.")
    else:
        print(f"Folder '{folder_path}' sudah ada.")

def capture_image(folder_name):
    """Menangkap gambar dan menyimpannya di folder yang ditentukan."""
    # Membuat path lengkap untuk folder
    data_img_path = 'data/' + folder_name
    create_folder(data_img_path)

    # Inisialisasi webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Webcam tidak dapat diakses.")
        return

    image_count = len(os.listdir(data_img_path))  # Menghitung jumlah gambar yang ada
    image_number = image_count + 1  # Nomor gambar selanjutnya

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Tidak dapat menangkap gambar.")
            break

        # Menampilkan gambar dari webcam
        cv2.imshow('Webcam', frame)

        # Tunggu input dari pengguna
        key = cv2.waitKey(1)

        # Jika pengguna menekan 's', simpan gambar
        if key == ord('s'):
            image_name = f"{folder_name}_{image_number}.jpg"
            image_path = os.path.join(data_img_path, image_name)
            cv2.imwrite(image_path, frame)
            print(f"Gambar disimpan: {image_path}")
            image_number += 1  # Increment nomor gambar

        # Jika pengguna menekan 'q', keluar
        elif key == ord('q'):
            break

    # Lepaskan webcam dan tutup semua jendela
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Input nama folder dari pengguna
    folder_name = input("Masukkan nama folder untuk menyimpan gambar: ")
    capture_image(folder_name)
