import math
import numpy as np
from scipy.io.wavfile import read
from scipy.signal import decimate

print("Press 1 for sin wave")
print("Press 2 for cosine wave")
opt = int(input("Enter option: "))

file = open("data.txt", "w+")

if (opt == 1):
    for i in np.linspace(0, 1, int(input("Enter number of elements: "))):
        file.writelines(str(math.sin(2*math.pi*2000*i))+"\n")
elif (opt == 2):
    for i in np.linspace(0, 1, int(input("Enter number of elements: "))):
        file.writelines(str(math.cos(2*math.pi*2000*i))+"\n")

