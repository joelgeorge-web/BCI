import serial
import csv

ser = serial.Serial('COM10', baudrate=230400)

csv_file_path = 'Reading1.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Time", "analogValue1", "analogValue2"])

    try:
        while True:
            # Read data from the serial port and print the raw data
            raw_data = ser.readline()

            # Decode data and handle errors
            data = raw_data.decode('utf-8', errors='replace').strip()

            # Split the data into parts using '|'
            data_parts = data.split(' ')

            # if len(data_parts) == 3:  # Three parts: "Time", "analogValue1", "analogValue2"
            elapsed_time = data_parts[0]
            analog_value_1 = data_parts[1]
            analog_value_2 = data_parts[2]

                # Display the information in the Python terminal
            print(f"Stopwatch Time: {elapsed_time} ms,  {analog_value_1},  {analog_value_2}")

                # Write the data to the CSV file
            csv_writer.writerow([elapsed_time, analog_value_1 , analog_value_2])
            

    except KeyboardInterrupt:
        ser.close()
        csv_file.close()
        print("Serial port and CSV file closed.")