import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Get seaborn dataset names
print(sns.get_dataset_names())

# Load penguins dataset
df = sns.load_dataset('penguins')

# Display first 10 rows
print(df.head(10))

# Display shape
print(df.shape)

# Display last few rows
print(df.tail())

# Check for null values
print(df.isnull().sum())

# Display basic statistics
print(df.describe())

# Display data types
print(df.dtypes)

# Display dataset info
print(df.info())

# Display all statistics including categorical
print(df.describe(include='all'))

# Display correlation matrix
print(df.corr(numeric_only=True))

# Create heatmap of correlations
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()

# Create histograms
df.select_dtypes(include=[np.number]).hist(figsize=(12,8))
plt.show()

# Create box plots
df.select_dtypes(include=[np.number]).plot(kind='box', subplots=True, layout=(3,2), sharex=False, sharey=False, figsize=(8,12))
plt.show()

# Display value counts
print(df.sex.value_counts())
print(df.island.value_counts())
print(df.species.value_counts())

# Create count plots
sns.countplot(data=df, x='sex')
plt.show()

sns.countplot(data=df, x='island')
plt.show()

sns.countplot(data=df, x='species')
plt.show()

sns.countplot(data=df, x='sex', hue='species')
plt.show()

sns.countplot(data=df, x='island', hue='species')
plt.show()

sns.countplot(data=df, x='island', hue='sex')
plt.show()

# Create pairplot
sns.pairplot(data=df, hue="species")
plt.show()