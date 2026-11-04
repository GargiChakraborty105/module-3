# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


from google.colab import files

# Upload File
uploaded = files.upload()

filename = list(uploaded.keys())[0]

# Load dataset
HouseDF = pd.read_csv(filename)

# Display first few rows
HouseDF.head()

# Dataset information
HouseDF.info()

# Statistical summary
HouseDF.describe()

# Column names
HouseDF.columns

# Pairplot for numerical features
sns.pairplot(HouseDF)

# Correlation heatmap
plt.figure(figsize=(8,6))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap='coolwarm',
    linewidths=0.5
)

plt.title("Correlation Heatmap")
plt.show()