import pandas as pd

# Load the original file
eng_df = pd.read_csv('eng.csv')

# Load the file to augment
augmented_df = pd.read_csv('augmented_randomized.csv')

# Get the last ID number from eng.csv
last_id = 2768  # Since the last id in eng.csv is 'eng_train_track_a_02768'

# Create new IDs for each row in augmented_randomized.csv starting from 02769
new_ids = [f'eng_train_track_a_{str(last_id + i + 1).zfill(5)}' for i in range(len(augmented_df))]

# Add the new IDs as a column in augmented_df
augmented_df.insert(0, 'id', new_ids)

# Concatenate the two DataFrames
combined_df = pd.concat([eng_df, augmented_df], ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv('eng_augmented.csv', index=False)

print("File 'eng_augmented.csv' has been created successfully.")
