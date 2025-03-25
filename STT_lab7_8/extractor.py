import os
import json

# Folder path containing the .sech (JSON) files
folder_path1 = '/Users/kushalrathod/Desktop/Projects/STT_lab7_8/ha_xiaomi_home/bandit_results'

# Output dictionary to store _totals from each file
totals_data1 = {}

# Loop through all files in the folder
for filename in os.listdir(folder_path1):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path1, filename)
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                # Extracting _totals if it exists
                if 'metrics' in data and '_totals' in data['metrics']:
                    totals_data1[filename] = data['metrics']['_totals']
        except Exception as e:
            print(f"Error reading {filename}: {e}")


folder_path2 = '/Users/kushalrathod/Desktop/Projects/STT_lab7_8/latexify_py/bandit_results'

# Output dictionary to store _totals from each file
totals_data2 = {}

# Loop through all files in the folder
for filename in os.listdir(folder_path2):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path2, filename)
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                # Extracting _totals if it exists
                if 'metrics' in data and '_totals' in data['metrics']:
                    totals_data2[filename] = data['metrics']['_totals']
        except Exception as e:
            print(f"Error reading {filename}: {e}")



folder_path3 = '/Users/kushalrathod/Desktop/Projects/STT_lab7_8/markitdown/bandit_results'
                

# Output dictionary to store _totals from each file
totals_data3 = {}

# Loop through all files in the folder
for filename in os.listdir(folder_path3):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path3, filename)
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                # Extracting _totals if it exists
                if 'metrics' in data and '_totals' in data['metrics']:
                    totals_data3[filename] = data['metrics']['_totals']
        except Exception as e:
            print(f"Error reading {filename}: {e}")

import matplotlib.pyplot as plt
import pandas as pd

# Convert dictionaries to DataFrames
df1 = pd.DataFrame.from_dict(totals_data1, orient='index')
df2 = pd.DataFrame.from_dict(totals_data2, orient='index')
df3 = pd.DataFrame.from_dict(totals_data3, orient='index')

# Extract CONFIDENCE.HIGH values
loc1 = df1['loc'].reset_index(drop=True)
loc2 = df2['loc'].reset_index(drop=True)
loc3 = df3['loc'].reset_index(drop=True)

# Plotting
plt.figure(figsize=(12, 6))

# Plot Dataset 1
plt.plot(loc1, label='Dataset 1', linestyle='-')

# Plot Dataset 2
plt.plot(loc2, label='Dataset 2', linestyle='--')

# Plot Dataset 3
plt.plot(loc3, label='Dataset 3', linestyle='-.')

# Labels and Title
plt.xlabel('File Index')
plt.ylabel('loc')
plt.title('loc Across Datasets')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()


# # Print or save the extracted _totals data
# for file, totals in totals_data1.items():
#     print(f"\n{totals}\n")
