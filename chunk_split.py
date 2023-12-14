import pandas as pd

# Load the original CSV file
original_file_path = 'Joel_jaw_clench.csv'
df = pd.read_csv(original_file_path)

# Specify the number of rows for each split
split_size = 977

# Calculate the number of splits needed
num_splits = (len(df) // split_size) + 1

# Split the DataFrame into chunks
split_data = [df.iloc[i*split_size:(i+1)*split_size] for i in range(num_splits)]

# Separate odd and even chunks
odd_chunks = [split_data[i] for i in range(0, num_splits, 2)]
even_chunks = [split_data[i] for i in range(1, num_splits, 2)]

# Save odd chunks to a new CSV file
odd_file_path = 'odd_chunks.csv'
pd.concat(odd_chunks).to_csv(odd_file_path, index=False)

# Save even chunks to a new CSV file
even_file_path = 'even_chunks.csv'
pd.concat(even_chunks).to_csv(even_file_path, index=False)

print("Splitting completed.")
