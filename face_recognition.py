
import os
import cv2
import numpy as np

dataset_path = "faces"

images = []
labels = []

for person in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person)

    if os.path.isdir(person_path):
        for image_name in os.listdir(person_path):
            image_path = os.path.join(person_path, image_name)

            img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            if img is not None:
                img = cv2.resize(img, (100, 100))
                images.append(img.flatten())
                labels.append(person)

print("Total Images Loaded:", len(images))
print("Total Labels Loaded:", len(labels))
from sklearn.decomposition import PCA

X = np.array(images)

pca = PCA(n_components=20)
X_pca = pca.fit_transform(X)

print("Original Shape:", X.shape)
print("PCA Shape:", X_pca.shape)
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
y = encoder.fit_transform(labels)

print("Number of Classes:", len(encoder.classes_))
print("Classes:", encoder.classes_)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X_pca,
    y,
    test_size=0.4,
    random_state=42
)

print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

ann = MLPClassifier(
    hidden_layer_sizes=(100,),
    max_iter=500,
    random_state=42
)

ann.fit(X_train, y_train)

y_pred = ann.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy * 100)
k_values = [5, 10, 15, 20, 25, 30]
accuracies = []
import matplotlib.pyplot as plt

k_values = [5, 10, 15, 20, 25, 30]
accuracies = []

for k in k_values:

    pca = PCA(n_components=k)
    X_pca = pca.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_pca,
        y,
        test_size=0.4,
        random_state=42
    )

    ann = MLPClassifier(
        hidden_layer_sizes=(100,),
        max_iter=500,
        random_state=42
    )

    ann.fit(X_train, y_train)

    y_pred = ann.predict(X_test)

    acc = accuracy_score(y_test, y_pred) * 100
    accuracies.append(acc)

    print("K =", k, "Accuracy =", acc)

plt.plot(k_values, accuracies, marker='o')
plt.xlabel("K Value")
plt.ylabel("Accuracy (%)")
plt.title("Accuracy vs K")
plt.grid(True)
plt.show()
test_image = cv2.imread("faces/Deepika/face_36.jpg", cv2.IMREAD_GRAYSCALE)

test_image = cv2.resize(test_image, (100, 100))
test_image = test_image.flatten().reshape(1, -1)

test_image_pca = pca.transform(test_image)

prediction = ann.predict(test_image_pca)

predicted_name = encoder.inverse_transform(prediction)

print("Predicted Person:", predicted_name[0])
unknown_image = cv2.imread("test_unknown.jpg", cv2.IMREAD_GRAYSCALE)

unknown_image = cv2.resize(unknown_image, (100, 100))
unknown_image = unknown_image.flatten().reshape(1, -1)

unknown_pca = pca.transform(unknown_image)

prediction = ann.predict(unknown_pca)

probabilities = ann.predict_proba(unknown_pca)
confidence = np.max(probabilities)

print("Confidence:", confidence)

predicted_name = encoder.inverse_transform(prediction)

if confidence < 0.90:
    print("Not Enrolled Person")
elif predicted_name[0] == "Unknown":
    print("Not Enrolled Person")
else:
=======
import os
import cv2
import numpy as np

dataset_path = "faces"

images = []
labels = []

for person in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person)

    if os.path.isdir(person_path):
        for image_name in os.listdir(person_path):
            image_path = os.path.join(person_path, image_name)

            img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            if img is not None:
                img = cv2.resize(img, (100, 100))
                images.append(img.flatten())
                labels.append(person)

print("Total Images Loaded:", len(images))
print("Total Labels Loaded:", len(labels))
from sklearn.decomposition import PCA

X = np.array(images)

pca = PCA(n_components=20)
X_pca = pca.fit_transform(X)

print("Original Shape:", X.shape)
print("PCA Shape:", X_pca.shape)
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
y = encoder.fit_transform(labels)

print("Number of Classes:", len(encoder.classes_))
print("Classes:", encoder.classes_)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X_pca,
    y,
    test_size=0.4,
    random_state=42
)

print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

ann = MLPClassifier(
    hidden_layer_sizes=(100,),
    max_iter=500,
    random_state=42
)

ann.fit(X_train, y_train)

y_pred = ann.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy * 100)
k_values = [5, 10, 15, 20, 25, 30]
accuracies = []
import matplotlib.pyplot as plt

k_values = [5, 10, 15, 20, 25, 30]
accuracies = []

for k in k_values:

    pca = PCA(n_components=k)
    X_pca = pca.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_pca,
        y,
        test_size=0.4,
        random_state=42
    )

    ann = MLPClassifier(
        hidden_layer_sizes=(100,),
        max_iter=500,
        random_state=42
    )

    ann.fit(X_train, y_train)

    y_pred = ann.predict(X_test)

    acc = accuracy_score(y_test, y_pred) * 100
    accuracies.append(acc)

    print("K =", k, "Accuracy =", acc)

plt.plot(k_values, accuracies, marker='o')
plt.xlabel("K Value")
plt.ylabel("Accuracy (%)")
plt.title("Accuracy vs K")
plt.grid(True)
plt.show()
test_image = cv2.imread("faces/Deepika/face_36.jpg", cv2.IMREAD_GRAYSCALE)

test_image = cv2.resize(test_image, (100, 100))
test_image = test_image.flatten().reshape(1, -1)

test_image_pca = pca.transform(test_image)

prediction = ann.predict(test_image_pca)

predicted_name = encoder.inverse_transform(prediction)

print("Predicted Person:", predicted_name[0])
unknown_image = cv2.imread("test_unknown.jpg", cv2.IMREAD_GRAYSCALE)

unknown_image = cv2.resize(unknown_image, (100, 100))
unknown_image = unknown_image.flatten().reshape(1, -1)

unknown_pca = pca.transform(unknown_image)

prediction = ann.predict(unknown_pca)

probabilities = ann.predict_proba(unknown_pca)
confidence = np.max(probabilities)

print("Confidence:", confidence)

predicted_name = encoder.inverse_transform(prediction)

if confidence < 0.90:
    print("Not Enrolled Person")
elif predicted_name[0] == "Unknown":
    print("Not Enrolled Person")
else:
>>>>>>> a5f3786d0532514eca31d64dbdef3d6a102de096
    print("Predicted Person:", predicted_name[0])