import math
import numpy as np
from scipy.io import wavfile
# from scipy.io.wavfile import read
# from scipy.signal import decimate

print("Press 1 for sin wave")
print("Press 2 for cosine wave")
print("Press 3 for using custom audio file (wav format)")
opt = int(input("Enter option: "))

file = open("data.txt", "w+")

if (opt == 1):
    for i in np.linspace(0, 1, int(input("Enter number of elements: "))):
        file.writelines(str(math.sin(2*math.pi*2000*i))+"\n")
elif (opt == 2):
    for i in np.linspace(0, 1, int(input("Enter number of elements: "))):
        file.writelines(str(math.cos(2*math.pi*2000*i))+"\n")
elif (opt == 3):
    file_name = input("Enter audio file name: ")
    samplerate, data = wavfile.read(file_name)
    for i in data:
        file.writelines(str(i[0]) + "\n")

