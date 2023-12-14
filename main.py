import serial
import csv

ser = serial.Serial('COM10', baudrate=230400)

csv_file_path = 'output_data.csv'
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
            data_parts = data.split('|')

            # Check if the data format is correct
            if len(data_parts) == 3 and data_parts[0].startswith("Time:"):
                try:
                    # Extract values from data parts
                    elapsed_time = int(data_parts[0].split(":")[1].strip())
                    analog_value_1 = int(data_parts[1].split(":")[1].strip())
                    analog_value_2 = int(data_parts[2].split(":")[1].strip())

                    # Display the information in the Python terminal
                    print(f"Stopwatch Time: {elapsed_time} ms,  {analog_value_1},  {analog_value_2}")

                    # Write the data to the CSV file
                    csv_writer.writerow([elapsed_time, analog_value_1, analog_value_2])

                except ValueError as e:
                    print(f"Error processing data: {e}")

            else:
                print(f"Unexpected data format: {data}")

    except KeyboardInterrupt:
        ser.close()
        csv_file.close()
        print("Serial port and CSV file closed.")
