# AI-sustainable-brick-detector
# AI-Based Acoustic Non-Destructive Brick Quality Detection System

# Structural Quality Assessment via Sound-Wave Feature Engineering and Machine Learning

This project is an automated, low-cost, non-destructive testing (NDT) system designed to assess the structural integrity of construction bricks. By capturing and analyzing the acoustic vibration signature of a brick when struck, the system extracts key physical features and utilizes a machine learning model to classify the material's quality in real time without causing physical damage.

Built as a 2nd-semester project at **Dayananda Sagar College of Engineering (DSCE)**, Bangalore.

## Problem Statement
Traditional compressive strength testing of construction materials relies heavily on destructive methods, which crush specimens, waste physical material, and require expensive laboratory equipment. Furthermore, manual acoustic assessments (such as hand-tapping with a hammer) suffer from high human inconsistency, subjective audio evaluation, and poor environmental noise rejection, leading to unreliable field quality control.

## The Solution: Automated Non-Destructive Evaluation (NDE)
We developed an end-to-end automated testing fixture that combines mechanical consistency, embedded data acquisition, and edge computing inference. The system runs an automated testing routine to classify specimens into one of three structural categories:
* **HIGH Quality:** Densely cured, high structural bonding (e.g., fully cured or cement-stabilized bricks).
* **MEDIUM Quality:** Intermediate density or under-cured porous variations.
* **LOW Quality:** Weak structural integration, cracked interiors, or traditional under-fired clay.

## Hardware Architecture

| Component | Role | Details |
| :--- | :--- | :--- |
| **Arduino Uno** | Central Data Acquisition Unit | Controls impact timing, samples raw sensor data, and extracts acoustic features |
| **12V Push-Pull Solenoid** | Repeatable Impact Actuator | Delivers consistent, uniform mechanical force to eliminate human manual tapping errors |
| **27mm Piezoelectric Disc** | Acoustic Vibration Sensor | Converts internal structural stress waves into analog voltage tracking signals |
| **16x2 I2C LCD** | Local User Interface | Displays real-time calibration states, test progress, and final AI quality predictions |

### Key Engineering Takeaway: Signal Stabilization & Sensor Contact
During early development, the piezoelectric sensor output exhibited severe noise and data drift (e.g., highly fluctuating baseline readings ranging from 180 to 600) due to solenoid mechanical recoil and imperfect physical contact with rough brick surfaces.

To solve this, we developed a dedicated **Piezo Monitoring Mode** in software. This loop actively reads the sensor's resting state, allowing the operator to adjust the physical placement and tension of the disc until the signal stays completely flat. The system blocks automated testing until the sensor baseline is stabilized, ensuring clean data collection.

## Control & Feature Extraction Logic (C++)

The microcontroller operates a sampling routine that collects a 300-sample signal window immediately following each solenoid strike, processing three engineered features: **Peak Amplitude**, **Total Energy**, and **Signal Decay Time**.

The codes used is attached in the repositroy.

## Machine Learning Integration

The backend software pipeline uses a **Random Forest Classifier** trained and deployed via Python (`train.py` and `deploy.py`). Feature importance analysis showed that **Signal Decay Time** and **Total Energy** contributed the most heavily to classification performance, whereas **Peak Value** alone was too sensitive to placement variations.

```text
[Hardware Setup] ──> Extracts Features (Peak, Energy, Decay) ──> Sent over Serial ──> [Python Inference (deploy.py)]
                                                                                                │
[LCD Displays Quality] <── Prints Result (HIGH / MEDIUM / LOW) <── Returns Label <── [Random Forest Model (Scikit-Learn)]

```

## Limitations

While the system successfully classifies specimens, specific engineering dependencies present future design boundaries:

* **Surface Roughness Dependency:** Variations in the physical face texture of bricks alter sensor coupling efficiency, requiring a strict physical mount layout.
* **Tethered Computer Dependency:** The Random Forest model runs externally in Python on a PC, requiring a persistent USB serial connection to execute inference.
* **Ambient Workspace Noise:** Excessive background shock waves or high-frequency laboratory table vibrations can bleed into the 300-sample tracking window.

## Future Outlook

* **Edge AI Deployment (TinyML):** Quantizing the Random Forest classifier or compiling a shallow Neural Network directly into the Arduino microcontroller code using Edge Impulse to make it fully standalone.
* **Wireless Fleet Mesh (ESP32):** Shifting from wired serial to wireless Bluetooth/Wi-Fi communication, streaming quality analysis vectors to a centralized site engineering dashboard.
* **Sorting Conveyor Mechanization:** Interfacing the system output with an automated servo-controlled actuator arm to automatically sorting sub-par bricks off an active industrial track line.
* **Better Sensor Integration:** A soldered piezo sensor would be more reliable in reading the signals and a bigger surface area of the sensor would be better suited for larger brick testing.

## Credits and Acknowledgments

* **Project Title**: AI Brick Sustainability Detector (Brick Quality Detection System)
* **Institution**: Dayananda Sagar College of Engineering (DSCE), Bangalore
* **Department**: Electronics and Communication Engineering
* **Course**: Interdisciplinary Project Based Learning (2nd Semester)

**Supervised by**: Prof. Nirmala Y.N of Electronics and Communications Department and Prof. Vidyashree J.C of Civil Department.
