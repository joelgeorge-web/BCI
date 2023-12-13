import serial
import csv

# Open the serial port
ser = serial.Serial('COM10', baudrate=9600)  # Adjust baudrate as needed

# Open a CSV file for writing
csv_file_path = 'output_data.csv'
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    try:
        while True:
            # Read data from the serial port
            data = ser.readline().decode('utf-8').strip()

            # Check if the data is a 3-digit number
            if data.isdigit() and len(data) == 3:
                # Display the 3-digit number in the Python terminal
                print(f"Received: {data}")

                # Write the data to the CSV file
                csv_writer.writerow([data])

            else:
                # Print a message for unexpected data
                print(f"Unexpected data: {data}")

    except KeyboardInterrupt:
        # Close the serial port and CSV file when the user interrupts the program
        ser.close()
        csv_file.close()
        print("Serial port and CSV file closed.")
