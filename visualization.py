import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path to the directory containing the files
directory = "DM Project/Individual Class Data"

# List all files in the directory
file_names = os.listdir(directory)

# Read data from all files and concatenate them into one DataFrame
dfs = []
for file in file_names:
    if file.endswith(".csv"):
        file_path = os.path.join(directory, file)
        df = pd.read_csv(file_path)
        dfs.append(df)

# Concatenate all DataFrames
df = pd.concat(dfs, ignore_index=True)

# Summary statistics
summary = df.describe()
print(summary)

# Pairplot
sns.pairplot(df, hue='Grade', diag_kind='kde')
plt.show()

# Boxplot
df.boxplot(by='Grade', layout=(2,2), figsize=(10, 10))
plt.show()

# Correlation heatmap
# Encode Grade column to numerical values
df['Grade'] = df['Grade'].map({'Pass': 1, 'Fail': 0})

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()
