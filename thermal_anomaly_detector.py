import machine
import time
import math

# Initialize the Pico's built-in internal temperature sensor
# Channel 4 is connected to the internal temp sensor on the RP2350
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / 65535

print("[TinyML] Calibrating Internal Chip Baseline (5 seconds)... Do not touch chip!")

baseline_samples = []
for i in range(5):
    raw_value = sensor_temp.read_u16()
    voltage = raw_value * conversion_factor
    # Temperature calculation formula for RP2350/RP2040 internal sensor
    temperature = 27 - (voltage - 0.706) / 0.001721
    baseline_samples.append(temperature)
    print(f"Sample {i+1}: {temperature:.2f}°C")
    time.sleep(1)

mean_temp = sum(baseline_samples) / len(baseline_samples)
std_temp = max(math.sqrt(sum((x - mean_temp)**2 for x in baseline_samples) / len(baseline_samples)), 0.1)

print(f"\n[Model Trained] Baseline Temp: {mean_temp:.2f}°C | Variance tolerance set.")
print("Starting Edge AI Real-Time Monitoring Loop (Try gently pressing your finger on the chip to heat it up)...")

while True:
    raw_value = sensor_temp.read_u16()
    voltage = raw_value * conversion_factor
    current_temp = 27 - (voltage - 0.706) / 0.001721
    
    # Compute Edge AI anomaly score (Z-score distance from baseline)
    z_score = abs(current_temp - mean_temp) / std_temp
    
    if z_score > 3.0:
        print(f"⚠️ THERMAL ANOMALY DETECTED! Score: {z_score:.2f} | Temp: {current_temp:.2f}°C")
    else:
        print(f"✅ NORMAL | Score: {z_score:.2f} | Temp: {current_temp:.2f}°C")
        
    time.sleep(1)