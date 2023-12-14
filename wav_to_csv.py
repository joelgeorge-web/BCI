# import sys, os, os.path
# from scipy.io import wavfile
# import pandas as pd

# input_filename = 'BYB_Recording_2023-12-13_11.47.15.wav'
# if input_filename[-3:] != 'wav':
#     print('WARNING!! Input File format should be *.wav')
#     sys.exit()

# sample_rate, data = wavfile.read(str(input_filename))
# print('Load is Done! \n')
# wavData = pd.DataFrame(data)
# print('Multi channel .wav file\n')
# print('number of channel : ' + str(len(wavData.columns)))
# wavData.to_csv(str(input_filename[:-4] + "Output_multi_channel.csv"), mode='w')
# print('Save is done ' + str(input_filename[:-4]) + 'Output_multi_channel.csv')


import sys
import os
from scipy.io import wavfile
import pandas as pd

# Specify the folder containing WAV files
input_folder = 'wavfile'

# Create an "output" folder if it doesn't exist
output_folder = 'output_beta'
os.makedirs(output_folder, exist_ok=True)

# Process all WAV files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".wav"):
        input_filepath = os.path.join(input_folder, filename)

        # Read WAV file
        sample_rate, data = wavfile.read(input_filepath)
        print(f'Loaded {filename}\n')

        # Convert to DataFrame
        wav_data = pd.DataFrame(data)
        print(f'Multi-channel WAV file\n')
        print(f'Number of channels: {len(wav_data.columns)}')

        # Save CSV file in the "output" folder with the same name as the WAV file
        output_filepath = os.path.join(output_folder, f"{filename[:-4]}.csv")
        wav_data.to_csv(output_filepath, mode='w', index=False)
        print(f'Saved {filename[:-4]}\n')

print('Conversion of all WAV files to CSV is complete.')
