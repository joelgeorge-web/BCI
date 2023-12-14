import serial
import csv
import time

# Define the serial port and baud rate
ser = serial.Serial('COM10', 230400)  # Replace 'COM3' with your actual serial port

# Create a CSV file and write headers
csv_filename = 'output_data.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    fieldnames = ['time', 'analogValue1', 'analogValue2']
    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csv_writer.writeheader()

    try:
        while True:
            # Read a line from the serial port
            line = ser.readline().decode('utf-8').strip()

            # Split the line into individual values
            values = line.split()

            # If there are three values (time, a1, a2), write them to the CSV file
            if len(values) == 3:
                data_dict = {'time': values[0], 'analogValue1': values[1], 'analogValue2': values[2]}
                csv_writer.writerow(data_dict)

                # Optional: Print the received data to the console
                print(data_dict)

            # Add a delay if needed to avoid high CPU usage
            time.sleep(0.1)

    except KeyboardInterrupt:
        # Close the serial port and exit gracefully if interrupted
        ser.close()
        print("\nSerial port closed. Exiting.")
