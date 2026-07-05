#  Face Recognition System using PCA & ANN

A Face Recognition System developed using **Python**, **OpenCV**, **Principal Component Analysis (PCA)**, and **Artificial Neural Networks (ANN)**. The system identifies enrolled users by extracting facial features using PCA and classifying them with an ANN model. If an unknown face is detected, it displays **"Not Enrolled Person"**.

##  Features
- Face image preprocessing
- Face recognition using PCA & ANN
- Unknown person detection
- Automatic prediction of enrolled users
- Accuracy evaluation
- Accuracy vs. K graph visualization


https://github.com/user-attachments/assets/e334f13f-f579-418b-8d99-492d17a347a9

##  Technologies Used

- **Python** – Core programming language
- **OpenCV** – Image processing and preprocessing
- **NumPy** – Numerical and array operations
- **Scikit-learn** – PCA and machine learning utilities
- **Matplotlib** – Performance graph visualization
- **PCA** – Feature extraction and dimensionality reduction
- **ANN** – Face classification and recognition

##  How It Works

1. **Dataset Loading**  
   Loads facial images of different individuals from organized dataset folders.

2. **Image Preprocessing**  
   Converts images to grayscale, resizes them to a fixed size, and transforms them into numerical arrays.

3. **Feature Extraction using PCA**  
   Reduces high-dimensional facial image data while preserving the most important facial characteristics.

4. **Model Training**  
   Uses the extracted facial features to train the recognition model for identity classification.

5. **Face Prediction**  
   Processes a new face image and predicts the identity of the person.

6. **Unknown Person Detection**  
   If the face does not match an enrolled identity, the system displays **"Not Enrolled Person"**.

## Dataset Summary

- **Total Images:** 460
- **Number of Classes:** 10
- **Original Feature Shape:** `(460, 10000)`
- **PCA Feature Shape:** `(460, 20)`
- **Training Samples:** 276
- **Testing Samples:** 184

## Project Structure

    Face-Recognition-PCA-ANN/
    │
    ├── faces/
    │   ├── Aamir/
    │   ├── Ajay/
    │   ├── Akshay/
    │   ├── Alia/
    │   ├── Amitabh/
    │   ├── Deepika/
    │   ├── Disha/
    │   ├── Farhan/
    │   ├── Ileana/
    │   └── Unknown/
    │
    ├── face_recognition.py
    ├── requirements.txt
    └── README.md
    
## Future Improvements

- Real-time face recognition using webcam
- Improve accuracy with a larger dataset
- Add automatic face detection
- Develop a graphical user interface
- Integrate CNN-based deep learning models
- Deploy as a web application

##  Author

**Rakshitha V R**  
B.Tech Information Technology Student
