# Raspberry-Pi-Pico-2-W-PROJECTS
My learning journey building projects especially EDGE AI projects using the Raspberry Pi Pico 2 W


# 1. Edge AI Thermal Anomaly Detector
  **Real-Time TinyML Anomaly Detection on the Raspberry Pi Pico 2 W**

**Hardware used**: Raspberry Pi Pico 2 W
**Language**: MicroPython

An ultra-lightweight, self-contained Edge AI system designed to detect real-time hardware thermal anomalies at the silicon layer. Operating completely offline without cloud dependencies or external sensors, this project showcases resource-constrained intelligence running locally on the dual ARM Cortex-M33 / RISC-V **RP2350 microcontroller**.

1) **True "Edge" Autonomy (No Cloud, No External Wiring):** Processing occurs 100% on-device. There is zero network latency, no reliance on external servers, and total data privacy.
2) **Direct Silicon Telemetry:** Instead of measuring ambient room temperature, the project leverages the **RP2350’s internal die junction temperature sensor via ADC Channel 4**. It continuously monitors thermal dissipation of the processor chip itself.
3) **Statistical Machine Intelligence over Static Thresholds:** Traditional embedded systems rely on hardcoded temperature limits (e.g., `if temp > 35°C`). This system implements an adaptive **Z-Score Anomaly Detection Algorithm** during runtime. It dynamically learns baseline ambient conditions and flags sudden thermal anomalies (such as direct physical contact or unexpected chip load) relative to environmental variance.



# 2. Real-Time Morse Code Decoder 

* **Microcontroller used:** Raspberry Pi Pico 2 W
* **Prototyping:** 1x Breadboard, Jumper wires
* **Language:** Micropython

A hardware-software solution that transforms raw electrical contact into digital text. Built using MicroPython and a **Raspberry Pi Pico 2 W**, this project turns simple jump wires into an interactive telegraph key that decodes Morse code inputs into standard alphanumeric characters in real-time.

* **Real-Time Edge Detection:** Actively measures high/low signal transitions down to the millisecond using `time.ticks_ms()`.
* **Hardware De-bouncing Filter:** Includes a software-based 30ms anti-glitch filter to eliminate mechanical contact noise (switch bounce) when the jumper wires touch.
* **Onboard LED Diagnostics:** Uses the internal Pico 2 W green LED to provide instant visual feedback whenever a connection is established.
* **Fault-Tolerant Dictionary Parsing:** Gracefully catches invalid Morse sequences and prompts the operator to retry without crashing the loop.


*How it works:* Leaving the wires separate holds the pin `HIGH` (1). Tapping the two wire tips together shorts GP15 to Ground, dropping the pin value to `LOW` (0) and triggering the decoder.

---

## Decoding Rules

The script dynamically differentiates dots, dashes, and pauses based on duration thresholds:

| Signal Type | Duration Conditions | Console Output |
| :--- | :--- | :--- |
| **Dot (`.`)** | ≤ 250 milliseconds | Prints `.` |
| **Dash (`-`)** | > 250 milliseconds | Prints `-` |
| **Letter Gap** | 1500 milliseconds of silence | Automatically decodes buffer (e.g., `-> [A]`) |

---


