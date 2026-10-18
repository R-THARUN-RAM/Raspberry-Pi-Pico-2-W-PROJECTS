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

---
