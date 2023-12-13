import sys, os, os.path
from scipy.io import wavfile
import pandas as pd

input_filename = 'BYB_Recording_2023-12-13_11.47.15.wav'
if input_filename[-3:] != 'wav':
    print('WARNING!! Input File format should be *.wav')
    sys.exit()

sample_rate, data = wavfile.read(str(input_filename))
print('Load is Done! \n')
wavData = pd.DataFrame(data)
print('Multi channel .wav file\n')
print('number of channel : ' + str(len(wavData.columns)))
wavData.to_csv(str(input_filename[:-4] + "Output_multi_channel.csv"), mode='w')
print('Save is done ' + str(input_filename[:-4]) + 'Output_multi_channel.csv')