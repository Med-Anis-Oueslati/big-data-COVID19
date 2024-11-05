import os
import pandas as pd

# Define the path to your directory with CSV files
directory_path = r"C:\Users\Med Anis Oueslati\Desktop\mini-projet-BigData\csse_covid_19_daily_reports_us"

# Initialize an empty list to store DataFrames
dataframes = []

# Iterate over each file in the directory
for filename in os.listdir(directory_path):
    # Check if the file has a .csv extension
    if filename.endswith(".csv"):
        # Read the CSV file and append to the list
        file_path = os.path.join(directory_path, filename)
        df = pd.read_csv(file_path)
        dataframes.append(df)

# Concatenate all DataFrames
if dataframes:
    concatenated_df = pd.concat(dataframes, ignore_index=True)

    # Save the concatenated DataFrame to a single CSV file
    output_file_path = os.path.join(directory_path, "concatenated_all_data.csv")
    concatenated_df.to_csv(output_file_path, index=False)
    print(f"Concatenated CSV file saved to {output_file_path}")
else:
    print("No CSV files found in the specified directory.")
