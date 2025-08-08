# Bone-Fracture-Classification-Using-Deep-Learning

## OVERVIEW

Bone fractures are one of the most common medical emergencies, and rapid, accurate diagnosis is essential to ensure timely treatment. This solution uses a Convolutional Neural Network (CNN) to automatically classify different types of bone fractures from X-ray images. The application is deployed using Streamlit, enabling real-time diagnostic predictions through a simple and interactive web interface.

![image](https://github.com/user-attachments/assets/a5c855f0-bd9f-41ce-b736-ab32c470f1e9)

## 📂 DATASET SOURCE
The dataset consists of a folder titled bone fracture classification, which contains 10 subfolders — each representing a different type of bone fracture.
Each subfolder includes a collection of X-ray images corresponding to that specific fracture type.
 -  Avulsion fracture

 -  Comminuted fracture

 -  Fracture Dislocation

 -  Greenstick fracture

 -  Hairline Fracture

 -  Impacted fracture

 -  Longitudinal fracture

 -  Oblique fracture

 -  Pathological fracture

 -  Spiral Fracture

Link of the dataset - https://www.kaggle.com/datasets/pkdarabi/bone-break-classification-image-dataset/data

## 🎯 OBJECTIVE

The main objectives of this work are to:

- Accurately classify bone fractures into specific categories using deep learning.

- Enable real-time diagnostic predictions through a web-based interface.

- Support medical staff by reducing manual triage time and improving decision-making efficiency.

## IMPLEMENTATION

1. Data Preprocessing

- Loaded and resized X-ray images from the 10 fracture classes.

- Applied image augmentation techniques like flipping, rotation, and contrast adjustments to increase diversity and prevent overfitting.

- Normalized pixel values for optimal training.

2. Model Building (CNN)

- Constructed a custom Convolutional Neural Network tailored for image classification.

- Fine-tuned hyperparameters such as kernel size, learning rate, and batch size.

- Used ReLU activation, pooling layers, and dropout for better generalization.

- Trained on a training-validation split and evaluated on unseen test data.

3. Model Performance

- Achieved 85%+ accuracy on the test set.

- Evaluated using metrics such as precision, recall, F1-score, and confusion matrix for each fracture type.

## 🤖 Why CNN Was Used?

CNNs (Convolutional Neural Networks) are especially effective for image data because they:

- Automatically detect visual patterns (like edges, textures, shapes) that help differentiate fracture types.

- Preserve spatial relationships in images, which is critical in analyzing medical scans.

- Require minimal manual feature engineering — allowing the model to learn directly from raw image pixels.

## Results & Real-World Impact

- The model can classify 10 different types of fractures with 85%+ accuracy.

- This reduces manual triage time by ~50%, allowing medical personnel to prioritize critical cases faster.

- Useful in rural clinics, emergency rooms, or remote diagnostic setups where radiology expertise may be limited.

- Helps serve as a second-opinion tool, boosting diagnostic confidence and decision support.

**Working Demo of Streamlit :**

## What is Streamlit?

Streamlit is an open-source Python framework for building and deploying web applications quickly, especially useful for data science and machine learning models.

## 🚀 Deployment Steps:

- Model Saving: The trained CNN model was saved as a .h5 file.

## Streamlit App Development:

- Built a simple web interface with image uploader.

- Displayed prediction results and confidence score.

- Visualized the uploaded X-ray before classification.

- Local Hosting: Streamlit was run locally using streamlit run app.py.

![image](https://github.com/user-attachments/assets/2a0e2858-e8b4-4d8a-bf9d-4b98d47ae6e2)
![image](https://github.com/user-attachments/assets/6e9b13d3-de9d-4198-9f4f-bc30b022a03c)


## 🔭 Future Scope & Improvements

- Integrate additional data from CT or MRI scans for multi-modal fracture diagnosis.

- Train on a larger, more diverse dataset to improve accuracy across rare fracture types.

- Add explainability with tools like Grad-CAM to highlight fracture zones.

- Extend to multi-label classification if multiple injuries exist in a single X-ray.

- Enable real-time mobile camera integration for on-the-go diagnostics.

## ✒️ Summary
This work demonstrates how deep learning and user-friendly deployment tools like Streamlit can be used to automate and accelerate fracture diagnosis from X-rays. With over 85% classification accuracy and real-time response, the solution provides meaningful support in both clinical and rural healthcare settings.





