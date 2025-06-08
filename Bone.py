import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

model = load_model("bone_fracture_break_model.h5")

class_names = ['Avulsion fracture', 'Comminuted fracture', 'Fracture Dislocation',
               'Greenstick fracture', 'Hairline Fracture', 'Impacted fracture',
               'Longitudinal fracture', 'Oblique fracture', 'Pathological fracture',
               'Spiral Fracture']  
               
# Streamlit UI
st.title("Bone Fracture Type Classification")
st.write("Upload an X-ray image and get the predicted fracture type.")

uploaded_file = st.file_uploader("Choose and upload the X-ray image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert('RGB')
    st.image(img, caption='Uploaded X-ray', use_column_width=True)

    img = img.resize((256, 256))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0  

    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]
    confidence = np.max(prediction) * 100

    st.success(f"**Predicted Class:** {predicted_class}")
    st.info(f"**Confidence Score:** {confidence:.2f}%")
