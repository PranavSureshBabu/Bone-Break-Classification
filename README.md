# Bone-Fracture-Classification-Using-Deep-Learning

![image](https://github.com/user-attachments/assets/a5c855f0-bd9f-41ce-b736-ab32c470f1e9)


**About the Dataset :**

The dataset covers a range of bone fracture classes, such as avulsion fractures, comminuted fractures, fracture-dislocations, greenstick fractures, hairline fractures, impacted fractures, longitudinal fractures, oblique fractures, pathological fractures, and spiral fractures.

The dataset link can be found here - https://www.kaggle.com/datasets/pkdarabi/bone-break-classification-image-dataset

**Objective :**

The goal of this project is to classify X-ray or bone images into different categories indicating whether a bone is broken or not. This type of classification can assist in automated medical diagnosis. 

**Tools and Libraries used :**

* TensorFlow/Keras
* Matplotlib and Numpy
* Scikit learn metrics
* Streamlit - to upload the X-ray image and get the predicted fracture type

**Implementation :**

* CNN Model with Hyperparameter Tuning – A convolutional neural network is designed with adjustable parameters like filter size, kernel dimensions, dropout rate, and learning rate to optimize fracture classification accuracy.
* Training for 5 Epochs – The model is trained using medical X-ray images for five epochs to ensure a balance between learning efficiency and avoiding overfitting.
* Preprocessing & Augmentation – Images undergo resizing and normalization, enhancing generalization and robustness against variations in medical imaging.
* Streamlit Integration for Image Upload – A user-friendly web interface allows users to upload X-ray images, which are then processed and classified in real-time.
* Fracture Type Prediction – The trained model outputs the most likely fracture type (e.g., No Fracture, Simple Fracture, Complex Fracture) along with confidence scores for decision support.

**Working Demo of Streamlit :**

Run the following command in your terminal to run the app
![image](https://github.com/user-attachments/assets/2156fd07-7616-496c-882e-94a6f5d7bf54)

![image](https://github.com/user-attachments/assets/2a0e2858-e8b4-4d8a-bf9d-4b98d47ae6e2)
![image](https://github.com/user-attachments/assets/6e9b13d3-de9d-4198-9f4f-bc30b022a03c)








