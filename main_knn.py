import cv2
import joblib
import numpy as np
import pandas as pd 

color_data =pd.read_csv('colors.csv')
color_data.head()
X = color_data[['B','G','R']].values
y = color_data['color_name'].values

#Muat model KNN dan scaler
knn = joblib.load('knn_model.pkl')
scaler = joblib.load('knn_scaler.pkl')

#Inisialisasi kamera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

#Ambil pixel tengah gambar
    height, width, _ = frame.shape
    pixel_center = frame[height//2, width//2]

# Normalisasi pixel sebelum prediksi
    pixel_center_scaled = scaler.transform([pixel_center])

# Prediksi warna
    color_pred = knn.predict(pixel_center_scaled) [0]

#Tampilkan warna pada frame
    cv2.putText(frame, f'Color: {color_pred}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()