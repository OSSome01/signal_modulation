import numpy as np
import matplotlib.pyplot as plt
import math

def constrain(val, min, max):
    if val > max:
        return max
    elif val < min:
        return min
    else:
        return val

file_name = input("Enter input file name: ")
file_data = open(file_name, "r")

input_signal = []

for point in file_data:
    input_signal.append(float(point))

input_signal = np.array(input_signal)

mp = min(input_signal)
mu = constrain(float(input("Enter value of modulation index (0-1): ")), 0, 1)
fc = float(input("Enter value of carrier frequency: "))
Ac = abs(mp) / mu
time_gaps = 1 / (2*fc)
number_of_input_points = len(input_signal)
time_vector = np.linspace(0, 1, number_of_input_points)

carrier_signal = Ac*np.cos(2*np.pi*fc*time_vector)
output_signal = (Ac + input_signal)*np.cos(2*np.pi*fc*time_vector)

plt.subplot(3,1,1)
plt.title('Amplitude Modulation')
plt.plot(input_signal,'g')
plt.ylabel('Amplitude')
plt.xlabel('Input signal')

plt.subplot(3,1,2)
plt.plot(carrier_signal, 'r')
plt.ylabel('Amplitude')
plt.xlabel('Carrier signal')

plt.subplot(3,1,3)
plt.plot(output_signal, color="blue")
plt.ylabel('Amplitude')
plt.xlabel('Output signal')

plt.subplots_adjust(hspace=1)
plt.rc('font', size=30)

plt.show()