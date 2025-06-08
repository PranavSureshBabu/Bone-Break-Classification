# Bone-Break-Classification

![image](https://github.com/user-attachments/assets/a5c855f0-bd9f-41ce-b736-ab32c470f1e9)


**About the Dataset :**

The dataset covers a range of bone fracture classes, such as avulsion fractures, comminuted fractures, fracture-dislocations, greenstick fractures, hairline fractures, impacted fractures, longitudinal fractures, oblique fractures, pathological fractures, and spiral fractures.

**Objective :**

The goal of this project is to classify X-ray or bone images into different categories indicating whether a bone is broken or not. This type of classification can assist in automated medical diagnosis. 

**Tools and Libraries used :**

* TensorFlow/Keras
* Matplotlib and Numpy
* Scikit learn metrics
* Streamlit - to upload the X-ray image and get the predicted fracture type

**Implementation :**

*CNN Model with Hyperparameter Tuning – A convolutional neural network is designed with adjustable parameters like filter size, kernel dimensions, dropout rate, and learning rate to optimize fracture classification accuracy.

*Training for 5 Epochs – The model is trained using medical X-ray images for five epochs to ensure a balance between learning efficiency and avoiding overfitting.

*Preprocessing & Augmentation – Images undergo resizing and normalization, enhancing generalization and robustness against variations in medical imaging.

*Streamlit Integration for Image Upload – A user-friendly web interface allows users to upload X-ray images, which are then processed and classified in real-time.
![image](https://github.com/user-attachments/assets/901a59e0-5199-4f45-bcb8-6b7b9e7a4cb2)


Fracture Type Prediction – The trained model outputs the most likely fracture type (e.g., No Fracture, Simple Fracture, Complex Fracture) along with confidence scores for decision support.




