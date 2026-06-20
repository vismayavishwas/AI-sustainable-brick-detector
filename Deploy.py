import serial
import joblib
import pandas as pd
import time

# Load trained model
model = joblib.load("brick_model.pkl")

# Connect to Arduino
ser = serial.Serial("COM3", 115200, timeout=1)

# Give Arduino time to reset
time.sleep(3)

# clear startup message
ser.reset_input_buffer()

print("AI READY")
input("Press Enter to START testing...")
time.sleep(1)
ser.write(b's\n')
print("START command sent")

while True:

    try:
        line = ser.readline().decode(errors="ignore").strip()

        if line:
            print(line)

        if line.startswith("FINAL"):

            _, peak, energy, decay_time = line.split(",")

            peak = float(peak)
            energy = float(energy)
            decay_time = float(decay_time)

            X = pd.DataFrame(
                [[peak, energy, decay_time]],
                columns=[
                    "peak",
                    "energy",
                    "decay_time"
                ]
            )

            prediction = model.predict(X)[0]

            print("\nPrediction:", prediction)

            # Send prediction back to Arduino
            ser.write((prediction + "\n").encode())

            print("Prediction sent to Arduino")

    except Exception as e:
        print("Error:", e)
        
