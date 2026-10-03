import tkinter as tk
from tkinter import messagebox
import pickle
import pandas as pd

# Load trained KNN model

with open("crop_knn_model.pkl", "rb") as file:
    model = pickle.load(file)


# Prediction function

def predict_crop():

    try:

        Nitrogen = float(entry_N.get())
        Phosphorus = float(entry_P.get())
        Potassium = float(entry_K.get())

        Temperature = float(
            entry_temperature.get()
        )

        Humidity  = float(
            entry_humidity.get()
        )

        pH_Value = float(
            entry_ph.get()
        )

        Rainfall = float(
            entry_rainfall.get()
        )


        # Input data
        input_data = pd.DataFrame([[
            Nitrogen,
            Phosphorus,
            Potassium,
            Temperature,
            Humidity,
            pH_Value,
            Rainfall    
        ]],columns=[
            "Nitrogen",
            "Phosphorus",
            "Potassium",
            "Temperature",
            "Humidity",
            "pH_Value",
            "Rainfall"
        ])


        # Predict crop
        prediction = model.predict(input_data)

        crop = prediction[0]


        # Display result
        result_label.config(
            text="Recommended Crop: " + crop
        )


    except ValueError:

        messagebox.showerror(
            "Input Error",
            "Please enter valid numbers."
        )


# Clear function

def clear_fields():

    entry_N.delete(0, tk.END)
    entry_P.delete(0, tk.END)
    entry_K.delete(0, tk.END)

    entry_temperature.delete(0, tk.END)
    entry_humidity.delete(0, tk.END)
    entry_ph.delete(0, tk.END)
    entry_rainfall.delete(0, tk.END)

    result_label.config(
        text="Recommended Crop: "
    )


# Main Window

window = tk.Tk()

window.title("Crop Recommendation System")

window.geometry("550x700")

window.resizable(False, False)


# Title

title = tk.Label(
    window,
    text="Crop Recommendation System",
    font=("Arial", 22, "bold")
)

title.pack(pady=20)


# Function to create input

def create_input(label_text):

    label = tk.Label(
        window,
        text=label_text,
        font=("Arial", 12)
    )

    label.pack(pady=(5, 0))

    entry = tk.Entry(
        window,
        font=("Arial", 12),
        width=25
    )

    entry.pack(pady=5)

    return entry


# Input fields

entry_N = create_input(
    "Nitrogen (N)"
)

entry_P = create_input(
    "Phosphorus (P)"
)

entry_K = create_input(
    "Potassium (K)"
)

entry_temperature = create_input(
    "Temperature (°C)"
)

entry_humidity = create_input(
    "Humidity (%)"
)

entry_ph = create_input(
    "Soil pH"
)

entry_rainfall = create_input(
    "Rainfall (mm)"
)


# Predict Button

predict_button = tk.Button(
    window,
    text="Recommend Crop",
    font=("Arial", 13, "bold"),
    command=predict_crop,
    width=20
)

predict_button.pack(pady=15)


# Clear Button


clear_button = tk.Button(
    window,
    text="Clear",
    font=("Arial", 12),
    command=clear_fields,
    width=15
)

clear_button.pack()


# Result

result_label = tk.Label(
    window,
    text="Recommended Crop: ",
    font=("Arial", 16, "bold")
)

result_label.pack(pady=30)


# Start application

window.mainloop()