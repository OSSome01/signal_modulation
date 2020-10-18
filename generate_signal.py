import math
import numpy as np
from scipy.io.wavfile import read
from scipy.signal import decimate

print("Press 1 for sin wave")
print("Press 2 for cosine wave")
print("Press 3 for using custom waveform audio file")
opt = int(input("Enter option: "))

file = open("data.txt", "w+")

if (opt == 1):
    for i in np.linspace(0, 1, int(input("Enter number of elements: "))):
        file.writelines(str(math.sin(2*math.pi*2000*i))+"\n")
elif (opt == 2):
    for i in np.linspace(0, 1, int(input("Enter number of elements: "))):
        file.writelines(str(math.cos(2*math.pi*2000*i))+"\n")
elif (opt == 3):
    wav_file = input("Enter name of audio file")
    wav_data = read(wav_file) 
    wav_array = np.array(wav_data[1], dtype=float)
    wav_array = decimate(wav_array, 50)
    file = open("data.txt", "w+")
    for i in wav_array:
        file.writelines(str(i) + "\n")
