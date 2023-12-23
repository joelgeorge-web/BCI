import serial
import torch
import torch.nn as nn
import numpy as np


# Configure the serial port (change port and baudrate as needed)
ser = serial.Serial('COM3', 9600, timeout=1)

# Create a buffer to store data
buffer_size = 5000
buffer = np.zeros((buffer_size, 2), dtype=int)

# Read data from Arduino and fill the buffer
for i in range(buffer_size):
    line = ser.readline().decode('utf-8').strip()
    values = list(map(int, line.split(',')))

    # Store data in the buffer
    buffer[i, :] = values

# Close the serial port
ser.close()

# Convert the buffer data to a PyTorch tensor
input_tensor = torch.tensor(buffer, dtype=torch.float32)

# Normalize or preprocess the input data if needed
# ...

# Make predictions using the pre-trained model
with torch.no_grad():
    output_tensor = model(input_tensor)

# Convert the output tensor to a NumPy array
predictions = output_tensor.numpy()

# Process or use the predictions as needed
# ...

print("Predictions:", predictions)
