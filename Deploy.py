import serial
import joblib
import pandas as pd

model = joblib.load("brick_model.pkl")

ser = serial.Serial("COM3", 115200)

print("AI READY 🔥")

while True:

    line = ser.readline().decode().strip()

    print(line)

    if line.startswith("FINAL"):

        try:
            _, peak, energy, decay, stability = line.split(",")

            peak = float(peak)
            energy = float(energy)
            decay = float(decay)
            stability = float(stability)

            X = pd.DataFrame([[
                peak,
                energy,
                decay,
                stability
            ]],
            columns=[
                'peak',
                'energy',
                'decay_time',
                'stability'
            ])

            prediction = model.predict(X)[0]

            print("Prediction:", prediction)

            ser.write((prediction + "\n").encode())

        except Exception as e:
            print("Error:", e)
