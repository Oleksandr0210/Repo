import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from tensorflow.keras.models import Sequential, load_model


st.title("Класифікація зображень за допомогою згорткових нейромереж")

st.sidebar.title("Налаштування")
model_choice = st.sidebar.selectbox("Оберіть модель:", ["Згорткова нейромережа", "VGG16"])
upload_image = st.sidebar.file_uploader("Завантажте зображення", type=["jpg", "jpeg", "png"])

if model_choice == "Згорткова нейромережа":
    model_path = "models/cnn_model.h5"
else:
    model_path = "models/vgg16_model.h5"

model = load_model(model_path)
st.sidebar.write("**Модель завантажено успішно!**")

def preprocess_image(image_path, target_size=(128, 128)):
    image = load_img(image_path, target_size=target_size)
    image_array = img_to_array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    return image, image_array

def display_training_graphs():
    st.subheader("Графіки навчання моделі")
    st.image("train_plot.png", caption="Функція втрат та точність", use_column_width=True)

if upload_image is not None:
    st.subheader("Завантажене зображення")
    image = Image.open(upload_image)
    st.image(image, caption="Вхідне зображення", use_column_width=True)

    _, preprocessed_image = preprocess_image(upload_image)

    st.subheader("Результати класифікації")
    predictions = model.predict(preprocessed_image)
    predicted_class = np.argmax(predictions)

    st.write("Ймовірності для кожного класу:")
    for i, prob in enumerate(predictions[0]):
        st.write(f"Клас {i}: {prob:.4f}")
    st.write(f"**Передбачений клас:** {predicted_class}")

    display_training_graphs()
else:
    st.info("Будь ласка, завантажте зображення для класифікації.")
    

model = Sequential([...])
model.compile(optimizer="adam", loss="categorical_crossentropy",
              metrics=["accuracy"])
model.fit(...)
model.save("models/cnn_model.h5")

vgg_model = Sequential([...])
vgg_model.compile(optimizer="adam",
                  loss="categorical_crossentropy", metrics=["accuracy"])
vgg_model.fit(...)
vgg_model.save("models/vgg16_model.h5")

history = 0

plt.figure(figsize=(10, 5))
plt.plot(history.history['accuracy'], label='Точність на тренуванні')
plt.plot(history.history['val_accuracy'], label='Точність на валідації')
plt.plot(history.history['loss'], label='Втрати на тренуванні')
plt.plot(history.history['val_loss'], label='Втрати на валідації')
plt.legend()
plt.savefig("train_plot.png")